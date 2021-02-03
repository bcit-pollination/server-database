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

CREATE TABLE Users (
    user_id 			INT 			NOT NULL 	AUTO_INCREMENT,
    first_name 			VARCHAR(40) 	NOT NULL,
    last_name 			VARCHAR(40) 	NOT NULL,
	email               VARCHAR(40)     NOT NULL,
	DOB                 DATE            NOT NULL,
	password_salt       VARCHAR(40)     NOT NULL,
	password_hash       VARCHAR(40)     NOT NULL,
    voting_token		VARCHAR(36) 	NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE Location (
    location_id 	INT 			NOT NULL 	AUTO_INCREMENT,
    country 		VARCHAR(40) 	NOT NULL,
    street_address 	VARCHAR(40) 	NOT NULL,
    city 			VARCHAR(40) 	NOT NULL,
    postal_code 	VARCHAR(20) 	NOT NULL,
    province_state 	VARCHAR(40) 	NOT NULL,
    PRIMARY KEY (location_id)
);

CREATE TABLE Vote (
    vote_id 		INT 		NOT NULL 	AUTO_INCREMENT,
    user_id 		INT 		NOT NULL,
    time_stamp 		TIMESTAMP 	NOT NULL 	DEFAULT(CURRENT_TIMESTAMP),
    PRIMARY KEY (vote_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Organization (
    org_id 		INT 			NOT NULL 	AUTO_INCREMENT,
    org_name 	VARCHAR(40) 	NOT NULL 	DEFAULT('Unknown'),
    PRIMARY KEY (org_id)
);

CREATE TABLE Enrollment (
    enrollment_id 		INT 			NOT NULL 	AUTO_INCREMENT,
    user_id 			INT 			NOT NULL,
    org_id 				INT 			NOT NULL,
    privilege_level 	INT 			NOT NULL 	DEFAULT(1), /* Lowest privilege level is 1. */
	identification 		VARCHAR(40)		NOT NULL,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (org_id)
        REFERENCES Organization (org_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Election (
    election_id 	INT 		NOT NULL 	AUTO_INCREMENT,
    org_id 			INT 		NOT NULL,
    start_time 		TIMESTAMP 	NOT NULL 	DEFAULT(CURRENT_TIMESTAMP),
    end_time 		TIMESTAMP 	NOT NULL 	DEFAULT(TIMESTAMPADD(day, 30, CURRENT_TIMESTAMP)),
    status 			ENUM('DRAFT', 'CALLED', 'ACTIVE', 'CLOSED', 'PUBLISHED') 
								NOT NULL 	DEFAULT('DRAFT'),
    is_anonymous 	BOOLEAN 	NOT NULL 	DEFAULT(TRUE),
    PRIMARY KEY (election_id),
    FOREIGN KEY (org_id)
        REFERENCES Organization (org_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Question (
    question_id 		INT 			NOT NULL 	AUTO_INCREMENT,
    election_id 		INT 			NOT NULL,
    description 		VARCHAR(40) 	NOT NULL,
    selection_limit 	INT 			NOT NULL,
    is_required 		BOOLEAN 		NOT NULL 	DEFAULT TRUE,
    PRIMARY KEY (question_id),
    FOREIGN KEY (election_id)
        REFERENCES Election (election_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Choice (
    choice_id 		INT 			NOT NULL 	AUTO_INCREMENT,
    question_id 	INT 			NOT NULL,
    description 	VARCHAR(40) 	NOT NULL,
    PRIMARY KEY (choice_id),
    FOREIGN KEY (question_id)
        REFERENCES Question (question_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Selection (
    selection_id 	INT 	NOT NULL 	AUTO_INCREMENT,
    vote_id 		INT 	NOT NULL,
    choice_id 		INT 	NOT NULL,
    PRIMARY KEY (selection_id),
    FOREIGN KEY (vote_id)
        REFERENCES Vote (vote_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (choice_id)
        REFERENCES Choice (choice_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Station (
    station_id 		INT 	NOT NULL 	AUTO_INCREMENT,
    election_id 	INT 	NOT NULL,
	location_id 	INT 	NOT NULL,
    PRIMARY KEY (station_id),
    FOREIGN KEY (election_id)
        REFERENCES Election (election_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (location_id)
        REFERENCES Location (location_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE RPI (
    rpi_id 		INT 		NOT NULL 	AUTO_INCREMENT,
    org_id 		INT 		NOT NULL,
    station_id 	INT,
    rpi_code 	VARCHAR(40) NOT NULL,
    PRIMARY KEY (rpi_id),
	FOREIGN KEY (org_id)
		REFERENCES Organization (org_id)
		ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (station_id)
        REFERENCES Station (station_id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Verifier (
    verifier_id 	INT 	NOT NULL 	AUTO_INCREMENT,
    user_id 		INT 	NOT NULL,
    station_id 		INT 	NOT NULL,
    PRIMARY KEY (verifier_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (station_id)
        REFERENCES Station (station_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

