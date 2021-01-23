DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Election;
DROP TABLE IF EXISTS Organization;
DROP TABLE IF EXISTS Vote;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users
(user_id         INT            NOT NULL    AUTO_INCREMENT       
,first_name      VARCHAR(40)    NOT NULL
,last_name       VARCHAR(40)    NOT NULL
,uuid            INT            NOT NULL
,identification  VARCHAR(40)    NOT NULL
,PRIMARY KEY (user_id)
);

CREATE TABLE Location
(location_id     INT            NOT NULL    AUTO_INCREMENT
,country         VARCHAR(40)    NOT NULL
,street_address  VARCHAR(40)    NOT NULL
,city            VARCHAR(40)    NOT NULL
,postal_code     VARCHAR(9)     NOT NULL
,province_state  VARCHAR(40)    NOT NULL
,PRIMARY KEY (location_id)
);

CREATE TABLE Vote
(vote_id         INT          NOT NULL     AUTO_INCREMENT
,user_id         INT          NOT NULL
,time_stamp      DATETIME     NOT NULL
,PRIMARY KEY (vote_id)
,CONSTRAINT FKvoteuserid
      FOREIGN KEY (user_id) REFERENCES Users(user_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE Organization
(org_id          INT          NOT NULL    AUTO_INCREMENT
,org_name        VARCHAR(40)  NOT NULL
,PRIMARY KEY (org_id)
);

CREATE TABLE Enrollment
(enrollment_id   INT          NOT NULL    AUTO_INCREMENT
,user_id         INT          NOT NULL
,org_id          INT          NOT NULL
,privilege_level INT          NOT NULL
,PRIMARY KEY (enrollment_id)
,CONSTRAINT FKenrollmentuserid
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
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
,start_time      DATETIME     NOT NULL
,end_time        DATETIME     NOT NULL
,status          VARCHAR(40)  NOT NULL
,is_published    BOOLEAN      NOT NULL
,is_anonymous    BOOLEAN      NOT NULL
,PRIMARY KEY (election_id)
, CONSTRAINT FKelectionorgid
      FOREIGN KEY(org_id) REFERENCES Organization(org_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);