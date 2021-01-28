DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Selection;
DROP TABLE IF EXISTS Choice;
DROP TABLE IF EXISTS Question;
DROP TABLE IF EXISTS RPI;
DROP TABLE IF EXISTS Verifier;
DROP TABLE IF EXISTS Station;
DROP TABLE IF EXISTS Election;
DROP TABLE IF EXISTS Organization;
DROP TABLE IF EXISTS Vote;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users
(user_id         INT            NOT NULL    AUTO_INCREMENT       
,first_name      VARCHAR(40)    NOT NULL    DEFAULT ('Unknown')
,last_name       VARCHAR(40)    NOT NULL    DEFAULT ('Unknown')
,uuid            BIGINT         NOT NULL    DEFAULT(0) /** UUID cannot be zero (zero indicates that UUID is unknown)*/
,identification  VARCHAR(40)    NOT NULL    DEFAULT ('Unknown')
,PRIMARY KEY (user_id)
);

CREATE TABLE Location
(location_id     INT            NOT NULL    AUTO_INCREMENT
,country         VARCHAR(40)    NOT NULL    DEFAULT ('Unknown')
,street_address  VARCHAR(40)    NOT NULL    DEFAULT ('Unknown')
,city            VARCHAR(40)    NOT NULL    DEFAULT ('Unknown')
,postal_code     VARCHAR(20)    NOT NULL    DEFAULT ('Unknown')
,province_state  VARCHAR(40)    NOT NULL    DEFAULT ('Unknown')
,PRIMARY KEY (location_id)
);

CREATE TABLE Vote
(vote_id         INT          NOT NULL     AUTO_INCREMENT
,user_id         INT          NOT NULL     
,time_stamp      TIMESTAMP    NOT NULL     DEFAULT (CURRENT_TIMESTAMP)
,PRIMARY KEY (vote_id)
,FOREIGN KEY (user_id) 
	REFERENCES Users(user_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE Organization
(org_id          INT          NOT NULL    AUTO_INCREMENT
,org_name        VARCHAR(40) /** Organization name can be null, 
                             but it's not recommended to leave blank.
                             It's not required to be filled out.*/
,PRIMARY KEY (org_id)
);

CREATE TABLE Enrollment
(enrollment_id   INT          NOT NULL    AUTO_INCREMENT
,user_id         INT          NOT NULL
,org_id          INT          NOT NULL
,privilege_level INT          NOT NULL    DEFAULT (1) /** 1 (I presume) is the lowest possible level
                                                 a user can be, so I msde it the default.*/
,PRIMARY KEY (enrollment_id)
,FOREIGN KEY (user_id) 
    REFERENCES Users(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
,CONSTRAINT FKenrollmentorgid
    FOREIGN KEY (org_id) REFERENCES Organization(org_id)	
    ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE Election
(election_id     INT          NOT NULL    AUTO_INCREMENT
,org_id          INT          NOT NULL
,start_time      TIMESTAMP    NOT NULL    DEFAULT(CURRENT_TIMESTAMP) /** Start date is automatically the first day the election was made.*/
,end_time        TIMESTAMP    NOT NULL    DEFAULT(TIMESTAMPADD(day, 30, CURRENT_TIMESTAMP)) /** End date is automatically thirty days after 
																	                        admin creates the election, if no other time is specified*/
,status          VARCHAR(40)  NOT NULL    DEFAULT ('Incomplete') /** Status is automatically incomplete unless otherwise specified.*/
,is_published    BOOLEAN      NOT NULL    DEFAULT (TRUE) /** Is published is automatically true. */
,is_anonymous    BOOLEAN      NOT NULL    DEFAULT (TRUE) /** It's anonymous automatically */
,PRIMARY KEY (election_id)
,FOREIGN KEY(org_id) 
      REFERENCES Organization(org_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE Question (
    question_id INT NOT NULL AUTO_INCREMENT,
    election_id INT NOT NULL,
    description VARCHAR(40) NOT NULL,
    selection_limit INT NOT NULL,
    is_required BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (question_id),
    FOREIGN KEY (election_id)
        REFERENCES Election (election_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Choice (
    choice_id INT NOT NULL AUTO_INCREMENT,
    question_id INT NOT NULL,
    description VARCHAR(40) NOT NULL,
    PRIMARY KEY (choice_id),
    FOREIGN KEY (question_id)
        REFERENCES Question (question_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Selection (
    selection_id INT NOT NULL AUTO_INCREMENT,
    vote_id INT NOT NULL,
    choice_id INT NOT NULL,
    PRIMARY KEY (selection_id),
    FOREIGN KEY (vote_id)
        REFERENCES Vote (vote_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (choice_id)
        REFERENCES Choice (choice_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Station (
    station_id INT NOT NULL AUTO_INCREMENT,
    election_id INT NOT NULL,
	location_id INT NOT NULL,
    PRIMARY KEY (station_id),
    FOREIGN KEY (election_id)
        REFERENCES Election (election_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (location_id)
        REFERENCES Location (location_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE RPI (
    rpi_id INT NOT NULL AUTO_INCREMENT,
    org_id INT NOT NULL,
    station_id INT,
    rpi_code VARCHAR(40) NOT NULL,
    PRIMARY KEY (rpi_id),
	FOREIGN KEY (org_id)
		REFERENCES Organization (org_id)
		ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (station_id)
        REFERENCES Station (station_id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Verifier (
    verifier_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    station_id INT NOT NULL,
    PRIMARY KEY (verifier_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (station_id)
        REFERENCES Station (station_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

