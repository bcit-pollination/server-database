DROP DATABASE IF EXISTS voting_system;
CREATE DATABASE voting_system;
USE voting_system;

CREATE TABLE Users (
    user_id 			INT 			NOT NULL 	AUTO_INCREMENT,
    first_name 			VARCHAR(40) 	NOT NULL,
    last_name 			VARCHAR(40) 	NOT NULL,
    email               VARCHAR(40)     NOT NULL	UNIQUE,
    dob                 DATE            NOT NULL,
    password	        VARCHAR(72)     NOT NULL,
    voting_token		VARCHAR(36) 	NOT NULL,
    deactivated			BOOLEAN			NOT NULL	DEFAULT(FALSE),
    PRIMARY KEY (user_id)
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
    disabled			BOOLEAN			NOT NULL    DEFAULT(FALSE),
    PRIMARY KEY (org_id)
);

CREATE TABLE Enrollment (
    enrollment_id 		INT 			NOT NULL 	AUTO_INCREMENT,
    user_id 			INT 			NOT NULL,
    org_id 				INT 			NOT NULL,
    privilege 	        INT 			NOT NULL 	DEFAULT(0), /* Lowest privilege level is 0. */
    user_org_id 		VARCHAR(40)     NOT NULL,
    inactive			BOOLEAN			NOT NULL 	DEFAULT(FALSE),
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (org_id)
        REFERENCES Organization (org_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE KEY (user_id, org_id),
    CHECK (privilege BETWEEN 0 AND 3)
);

CREATE TABLE Election (
    election_id 	            INT 		NOT NULL 	AUTO_INCREMENT,
    org_id 			            INT 		NOT NULL,
    election_description		VARCHAR(40)	NOT NULL,
    start_time 		            TIMESTAMP 	NOT NULL 	DEFAULT(CURRENT_TIMESTAMP),
    end_time 		            TIMESTAMP 	NOT NULL 	DEFAULT(TIMESTAMPADD(day, 30, CURRENT_TIMESTAMP)),
    anonymous 	                BOOLEAN 	NOT NULL 	DEFAULT(TRUE),
    public_results              BOOLEAN     NOT NULL    DEFAULT(FALSE),
    verified                    BOOLEAN     NOT NULL	DEFAULT(FALSE),
    PRIMARY KEY (election_id),
    FOREIGN KEY (org_id)
        REFERENCES Organization (org_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Question (
    question_id 		        INT 			NOT NULL 	AUTO_INCREMENT,
    election_id 		        INT 			NOT NULL,
    question_description 		VARCHAR(40) 	NOT NULL,
    max_selection_count         INT 			NOT NULL,
    PRIMARY KEY (question_id),
    FOREIGN KEY (election_id)
        REFERENCES Election (election_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Opt (
    option_id 		        INT 			NOT NULL 	AUTO_INCREMENT,
    question_id 	        INT 			NOT NULL,
    option_description      VARCHAR(40) 	NOT NULL,
    total_votes_for         INT				NOT NULL	DEFAULT 0,
    PRIMARY KEY (option_id),
    FOREIGN KEY (question_id)
        REFERENCES Question (question_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Choice (
    choice_id 	INT 	NOT NULL 	AUTO_INCREMENT,
    vote_id     INT 	NOT NULL,
    option_id 	INT 	NOT NULL,
    PRIMARY KEY (choice_id),
    FOREIGN KEY (vote_id)
        REFERENCES Vote (vote_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (option_id)
        REFERENCES Opt (option_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE KEY (vote_id, option_id)
);

