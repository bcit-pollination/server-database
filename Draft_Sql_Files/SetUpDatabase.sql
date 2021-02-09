DROP DATABASE IF EXISTS voting_system;
CREATE DATABASE voting_system;
USE voting_system;

CREATE TABLE Users (
    user_id 			INT 			NOT NULL 	AUTO_INCREMENT,
    first_name 			VARCHAR(40) 	NOT NULL,
    last_name 			VARCHAR(40) 	NOT NULL,
	email               VARCHAR(40)     NOT NULL	UNIQUE,
	date_of_birth       DATE            NOT NULL,
	password	        VARCHAR(72)     NOT NULL,
    voting_token		VARCHAR(36) 	NOT NULL,
    disabled			BOOLEAN			NOT NULL	DEFAULT(FALSE),
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
    org_id 				INT 			NOT NULL 	AUTO_INCREMENT,
    org_name 			VARCHAR(40) 	NOT NULL 	DEFAULT('Unknown'),
	verifier_password   VARCHAR(72)     NOT NULL,
    PRIMARY KEY (org_id)
);

CREATE TABLE Enrollment (
    enrollment_id 		INT 			NOT NULL 	AUTO_INCREMENT,
    user_id 			INT 			NOT NULL,
    org_id 				INT 			NOT NULL,
    privilege_level 	INT 			NOT NULL 	DEFAULT(0), /* Lowest privilege level is 0. */
	identification 		VARCHAR(40),
    disabled			BOOLEAN			NOT NULL 	DEFAULT(FALSE),
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (org_id)
        REFERENCES Organization (org_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
	UNIQUE KEY (user_id, org_id)
);

CREATE TABLE Election (
    election_id 	INT 		NOT NULL 	AUTO_INCREMENT,
    org_id 			INT 		NOT NULL,
    description		VARCHAR(40)	NOT NULL,
	verified        BOOLEAN     NOT NULL,
    start_time 		TIMESTAMP 	NOT NULL 	DEFAULT(CURRENT_TIMESTAMP),
    end_time 		TIMESTAMP 	NOT NULL 	DEFAULT(TIMESTAMPADD(day, 30, CURRENT_TIMESTAMP)),
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

