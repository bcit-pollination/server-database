USE voting_system;

DROP PROCEDURE IF EXISTS LoginUser;

DROP PROCEDURE IF EXISTS DeactivateUser;
DROP PROCEDURE IF EXISTS GetUser;
DROP PROCEDURE IF EXISTS CreateUser;
DROP PROCEDURE IF EXISTS GetUserToken;
DROP PROCEDURE IF EXISTS UpdateUser;

DROP PROCEDURE IF EXISTS DisbandOrg;
DROP PROCEDURE IF EXISTS GetOwnerOrgInfo;
DROP PROCEDURE IF EXISTS CreateOrg;
DROP PROCEDURE IF EXISTS UpdateOrg;
DROP PROCEDURE IF EXISTS UpdateUserOrgId;
DROP PROCEDURE IF EXISTS UpdateVerifierPassword;
DROP PROCEDURE IF EXISTS GetOrg;
DROP PROCEDURE IF EXISTS GetUserOrgId;
DROP PROCEDURE IF EXISTS GetVerifierPassword;
DROP PROCEDURE IF EXISTS GetUserOrgListInfo;

DROP PROCEDURE IF EXISTS GetUsersFromOrg;
DROP PROCEDURE IF EXISTS InviteUser;
DROP PROCEDURE IF EXISTS KickUser;
DROP PROCEDURE IF EXISTS UpdatePrivilege;
DROP PROCEDURE IF EXISTS GetPrivilege;

DROP PROCEDURE IF EXISTS DeleteElection;
DROP PROCEDURE IF EXISTS GetElection;
DROP PROCEDURE IF EXISTS CreateElection;
DROP PROCEDURE IF EXISTS UpdateElection;
DROP PROCEDURE IF EXISTS GetOrgElections;
DROP PROCEDURE IF EXISTS GetUserElections;

DROP PROCEDURE IF EXISTS AddQuestion;
DROP PROCEDURE IF EXISTS DeleteQuestion;
DROP PROCEDURE IF EXISTS UpdateQuestion;
DROP PROCEDURE IF EXISTS AddOption;
DROP PROCEDURE IF EXISTS DeleteOption;
DROP PROCEDURE IF EXISTS UpdateOption;
DROP PROCEDURE IF EXISTS GetQuestionOptions;
DROP PROCEDURE IF EXISTS GetQuestions;
DROP PROCEDURE IF EXISTS GetQuestionsAndOptions;

DROP PROCEDURE IF EXISTS GetUserVotes;

DROP PROCEDURE IF EXISTS AddVote;
DROP PROCEDURE IF EXISTS AddChoice;

DROP PROCEDURE IF EXISTS GetVoterList;

DROP PROCEDURE IF EXISTS GetPublicElections;

DROP PROCEDURE IF EXISTS GetElectionsAlternate;

DELIMITER //
//

/**
 * Returns the user_id correspoding to the email and password.
 */
CREATE PROCEDURE LoginUser(
    IN email VARCHAR(40),
    IN password VARCHAR(72))
BEGIN
    SELECT user_id FROM Users u
    WHERE u.email = email 
    AND u.password = password;
END; //

/**
 * Deactivates the user (also kicks them from their joined organizations).
 */
CREATE PROCEDURE DeactivateUser(
    IN user_id INT)
BEGIN
    UPDATE Users u
    SET deactivated = TRUE
    WHERE u.user_id = user_id;

    UPDATE Enrollment e
    SET inactive = TRUE
    WHERE e.user_id = user_id;
END; //

/**
 * Gets the user's non-sensitive data.
 */
CREATE PROCEDURE GetUser(
    IN user_id INT)
BEGIN
    SELECT user_id, first_name, last_name, email, dob 
    FROM Users u
    WHERE u.user_id = user_id;
END; //

/**
 * Creates a user with the specified data, 
 * returning the id of the created user.
 */
CREATE PROCEDURE CreateUser(
    IN first_name VARCHAR(40), 
    IN last_name VARCHAR(40), 
    IN email VARCHAR(40),
    IN dob DATE,
    IN password VARCHAR(40),
    IN voting_token VARCHAR(36))
BEGIN
    INSERT INTO Users(first_name, last_name, email, dob, 
        password, voting_token)
    VALUES(first_name, last_name, email, dob, 
        password, voting_token);
    SELECT LAST_INSERT_ID() AS `user_id`;
END; //

/**
 * Gets the user's voting_token.
 */
CREATE PROCEDURE GetUserToken(
    IN user_id INT)
BEGIN
    SELECT voting_token
    FROM Users u
    WHERE u.user_id = user_id;
END; //

/**
 * Updates a user's password.
 */
CREATE PROCEDURE UpdateUser(
    IN user_id INT,
    IN password VARCHAR(72))
BEGIN
    UPDATE Users u
    SET u.password = password
    WHERE u.user_id = user_id;
END; //



/**
 * Disbands an organization, kicking everyone
 * from the organization.
 * NOTE: This procedure can be done safely since we are not allowing for
 * a user to be the owner of more than one organization.
 */
CREATE PROCEDURE DisbandOrg(
    IN user_id INT)
BEGIN
    DECLARE org_id INT;
    
    SELECT o.org_id
    INTO org_id
    FROM Enrollment e
        INNER JOIN Organization o
            ON e.org_id = o.org_id
    WHERE e.user_id = user_id;

    UPDATE Organization o
    SET o.disabled = TRUE
    WHERE o.org_id = org_id;

    UPDATE Enrollment e
    SET e.inactive = TRUE
    WHERE e.org_id = org_id;
END; //

/**
 * Gets the org_id, org_name, privilege, and user_org_id
 * for the user's organization in which they are the owner.
 */
CREATE PROCEDURE GetOwnerOrgInfo(
    IN user_id INT)
BEGIN
    SELECT o.org_id, o.org_name, e.privilege, e.user_org_id FROM Users u
        INNER JOIN Enrollment e
            ON u.user_id = e.user_id
        INNER JOIN Organization o
            ON e.org_id = o.org_id
    WHERE e.user_id = user_id
    AND e.privilege = 3;
END; //

/**
 * Creates an organization with the given user_id, org_name, verifier_password,
 * as well as the owner's user_org_id.
 */
CREATE PROCEDURE CreateOrg(
    IN user_id INT, 
    IN org_name VARCHAR(40),
    IN verifier_password VARCHAR(72),
    IN user_org_id VARCHAR(40))
BEGIN
    INSERT INTO Organization(org_name, verifier_password)
    VALUES(org_name, verifier_password);
    SELECT LAST_INSERT_ID() AS `org_id`;
    INSERT INTO Enrollment(user_id, org_id, user_org_id, privilege)
    VALUES(user_id, LAST_INSERT_ID(), user_org_id, 3);
END; //

/** 
 * Updates an organization's name. 
 */
CREATE PROCEDURE UpdateOrg(
    IN org_id INT, 
    IN org_name VARCHAR(40))
BEGIN
    UPDATE Organization o
    SET o.org_name = org_name
    WHERE o.org_id = org_id;
END; //

/**
 * Updates the user_org_id of the specified user of the organization.
 */
 CREATE PROCEDURE UpdateUserOrgId(
     IN user_id INT,
     IN org_id INT,
     IN user_org_id VARCHAR(40))
 BEGIN
    UPDATE Enrollment e
    SET e.user_org_id = user_org_id
    WHERE e.user_id = user_id
    AND e.org_id = org_id;
 END; //

/** 
 * Updates the verifier password for the specified organization. 
 */
CREATE PROCEDURE UpdateVerifierPassword(
    IN org_id INT,
    IN verifier_password VARCHAR(72))
BEGIN
    UPDATE Organization o
    SET o.verifier_password = verifier_password
    WHERE o.org_id = org_id;
END; //


/** 
 * Gets an organization's id and name.
 */
CREATE PROCEDURE GetOrg(
    IN org_id INT)
BEGIN
    SELECT o.org_id, o.org_name FROM Organization o
    WHERE o.org_id = org_id;
END; //

/**
 * Gets the user_org_id of the specified user of the organization.
 */
 CREATE PROCEDURE GetUserOrgId(
     IN user_id INT,
     IN org_id INT)
 BEGIN
    SELECT user_org_id FROM Enrollment e
    WHERE e.user_id = user_id
    AND e.org_id = org_id;
 END; //

/** 
 * Gets the verifier password for the specified organization. 
 */
CREATE PROCEDURE GetVerifierPassword(
    IN org_id INT)
BEGIN
    SELECT verifier_password FROM Organization o
    WHERE o.org_id = org_id;
END; //

/**
 * Gets the org_id, org_name, privilege, and user_org_id
 * for the user's organizations in which they are a user.
 */
CREATE PROCEDURE GetUserOrgListInfo(
    IN user_id INT)
BEGIN
    SELECT o.org_id, o.org_name, e.privilege, e.user_org_id FROM Users u
        INNER JOIN Enrollment e
            ON u.user_id = e.user_id
        INNER JOIN Organization o
            ON e.org_id = o.org_id
    WHERE e.user_id = user_id
    AND e.privilege > 0;
END; //
 


/**
 * Gets a list of the users' user_id, first_name, last_name
 * email, dob, privilege, and user_org_id from an organization.
 */
CREATE PROCEDURE GetUsersFromOrg(
    IN org_id INT)
BEGIN
    SELECT u.user_id, u.first_name, u.last_name, u.email, u.dob, e.privilege, e.user_org_id 
    FROM Users u
        INNER JOIN Enrollment e
           ON e.user_id = u.user_id
        INNER JOIN Organization o
           ON o.org_id = e.org_id
    WHERE o.org_id = org_id
    AND e.privilege > 0;
END; //

/**
 * Invites a user to the specified organization.
 */
CREATE PROCEDURE InviteUser(
    IN email VARCHAR(40), 
    IN user_org_id VARCHAR(40),
    IN org_id INT)
BEGIN
    DECLARE user_id INT;
    
    SELECT u.user_id
    INTO user_id
    FROM Users u
    WHERE u.email = email;

    INSERT INTO Enrollment(user_id, org_id, user_org_id)
    VALUES(user_id, org_id, user_org_id);
END; //


/**
 * Kicks a user from the specified organization.
 */
CREATE PROCEDURE KickUser(
    IN user_id INT, 
    IN org_id INT)
BEGIN
    UPDATE Enrollment e
    SET e.inactive = TRUE
    WHERE e.user_id = user_id
    AND e.org_id = org_id;
END; //

/** 
 * Updates the privilege level of the specified user of the organization.
 */
CREATE PROCEDURE UpdatePrivilege(
    IN user_id INT,
    IN org_id INT,
    IN privilege INT)
BEGIN
    UPDATE Enrollment e
    SET e.privilege = privilege
    WHERE e.user_id = user_id
    AND e.org_id = org_id;
END; //

/** 
 * Gets the privilege level of the specified user of the organization.
 */
CREATE PROCEDURE GetPrivilege(
    IN org_id INT,
    IN user_id INT)
BEGIN
    SELECT e.privilege FROM Enrollment e
    WHERE e.org_id = org_id
    AND e.user_id = user_id;
END; //



/**
 * Deletes the specified election.
 */
CREATE PROCEDURE DeleteElection(
    IN election_id INT)
BEGIN
    DELETE FROM Election e
    WHERE e.election_id = election_id;
END; //

/**
 * Gets the details of a specified election, excluding the questions and options.
 */
CREATE PROCEDURE GetElection(
    IN election_id INT)
BEGIN
    SELECT * FROM Election e
        WHERE e.election_id = election_id;
END; //

/**
 * Creates an election with the specified parameters, returning the created election's id.
 */
CREATE PROCEDURE CreateElection(
    IN org_id INT, 
    IN election_description VARCHAR(40),
    IN start_time TIMESTAMP,
    IN end_time TIMESTAMP,
    IN anonymous BOOLEAN,
    IN public_results BOOLEAN,
    IN verified BOOLEAN)
BEGIN
    INSERT INTO Election(org_id, election_description, start_time, end_time, anonymous, public_results, verified)
    VALUES(org_id, election_description, start_time, end_time, anonymous, public_results, verified);
    SELECT LAST_INSERT_ID() AS `election_id`;
END;//

/**
 * Updates an election with the specified parameters.
 */
CREATE PROCEDURE UpdateElection(
    IN id INT,
    IN election_description VARCHAR(40),
    IN start_time TIMESTAMP,
    IN end_time TIMESTAMP,
    IN anonymous BOOLEAN,
    IN public_results BOOLEAN,
    IN verified BOOLEAN)
BEGIN
    UPDATE Election e
    SET e.election_description = election_description,
        e.start_time = start_time,
        e.end_time = end_time,
        e.anonymous = anonymous,
        e.public_results = public_results,
        e.verified = verified
    WHERE election_id = id;
END; //

/**
 * Gets the details of all elections of an organization,
 * excluding the questions and options.
 */
CREATE PROCEDURE GetOrgElections(
    IN org_id INT)
BEGIN
    SELECT e.* FROM Election e
        WHERE e.org_id = org_id;
END; //

/**
 * Gets the details of all elections of organizations a user belongs to,
 * excluding the questions and options.
 */
CREATE PROCEDURE GetUserElections(
    IN user_id INT)
BEGIN
    SELECT e.* FROM Users u
        INNER JOIN Enrollment e
            ON e.user_id = u.user_id
        INNER JOIN Election el
            ON e.org_id = el.org_id	
    WHERE e.user_id = user_id;
END; //


/**
 * Adds a question to an election.
 */
CREATE PROCEDURE AddQuestion(
    IN election_id INT,
    IN question_description VARCHAR(40),
    IN max_selection_count INT)
BEGIN
    INSERT INTO Question (election_id, question_description, max_selection_count)
        VALUES (election_id, question_description, max_selection_count);
END; //

/**
 * Deletes a question to an election.
 */
CREATE PROCEDURE DeleteQuestion(
    IN question_id INT)
BEGIN
    DELETE FROM Question q
    WHERE q.question_id = question_id;
END; //

/**
 * Updates the specified question.
 */
CREATE PROCEDURE UpdateQuestion(
    IN question_id INT,
    IN question_description VARCHAR(40))
BEGIN
    UPDATE Question q
        SET q.question_description = question_description
        WHERE q.question_id = question_id;
END; //
    

/** 
 * Adds a choice to a question. 
 */
CREATE PROCEDURE AddOption(
    IN question_id INT,
    IN option_description VARCHAR(40))
BEGIN
    INSERT INTO Opt (question_id, option_description) 
    VALUES(question_id, option_description);
    
    UPDATE Question q
        SET max_selection_count = max_selection_count + 1
        WHERE q.question_id = question_id;
END; //

/** 
 * Deletes a choice to a question. 
 */
CREATE PROCEDURE DeleteOption(
    IN option_id INT)
BEGIN
    UPDATE Question q
    INNER JOIN Opt o ON q.question_id = o.question_id
    SET q.max_selection_count = q.max_selection_count - 1
    WHERE o.option_id = option_id;
    
    DELETE FROM Opt o
    WHERE o.option_id = option_id; 
END; //

/** 
 * Updates a choice to a question. 
 */
CREATE PROCEDURE UpdateOption(
    IN option_id INT,
    IN option_description VARCHAR(40))
BEGIN
    UPDATE Opt o
    SET o.option_description = option_description
    WHERE o.option_id = option_id;
END; //



/**
 * Gets all the details about the specified question's options, 
 * including the total votes cast for each option.
 */
CREATE PROCEDURE GetQuestionOptions(
    IN question_id INT)
BEGIN
    SELECT o.* FROM Opt o
        WHERE o.question_id = question_id;
END; //

/** 
 * Gets all the questions from the specified election.
 */
CREATE PROCEDURE GetQuestions(
    IN election_id INT)
BEGIN
    SELECT q.* FROM Question q
        INNER JOIN Election e
        ON e.election_id = q.election_id
        WHERE q.election_id = election_id;
END; //

/** 
 * Gets all the questions and options from the specified election,
 * including the total votes cast for each option.
 */
CREATE PROCEDURE GetQuestionsAndOptions(
    IN election_id INT)
BEGIN
    SELECT q.*, o.* FROM Question q
        INNER JOIN Election e
        ON e.election_id = q.election_id
        INNER JOIN Opt o
        ON o.question_id = q.question_id
        WHERE q.election_id = election_id;
END; //



/**
 * Gets the first_name, last_name, question_id, question_description,
 * option_id, and option_description pertaining to each of the casted votes
 * for the specified election.
 */
CREATE PROCEDURE GetUserVotes(
    IN election_id INT)
BEGIN   
    SELECT u.first_name, u.last_name, q.question_id, q.question_description, 
        o.option_id, o.option_description FROM Election el
        INNER JOIN Question q
            ON el.election_id = q.election_id
        INNER JOIN Opt o
            ON q.question_id = o.question_id
        INNER JOIN Choice c
            ON o.option_id = c.option_id
        INNER JOIN Vote v
            ON c.vote_id = v.vote_id
        INNER JOIN Users u
            ON v.user_id = u.user_id;
END; //



/** 
 * Adds a vote, getting the ID if successfully added or updated.
 * Previously chosen options have their total_votes_for value
 * decremented if the vote was updated. 
 */
CREATE PROCEDURE AddVote(
    IN voting_token VARCHAR(36),
    IN time_stamp TIMESTAMP,
    IN election_id INT)
BEGIN
    DECLARE user_id INT;
    DECLARE prev_time_stamp TIMESTAMP;
    DECLARE vote_id INT;
    
    SELECT u.user_id
    INTO user_id
    FROM Users u
    WHERE u.voting_token = voting_token;

    SELECT v.time_stamp, v.vote_id
    INTO prev_time_stamp, vote_id
    FROM Users u
        INNER JOIN Vote v
            ON v.user_id = u.user_id
        INNER JOIN Enrollment e
            ON e.user_id = u.user_id
        INNER JOIN Organization o
            ON o.org_id = e.org_id
        INNER JOIN Election el
            ON el.org_id = o.org_id
    WHERE el.election_id = election_id;

    IF (prev_time_stamp IS NULL) THEN
        INSERT INTO Vote(user_id, time_stamp)
        VALUES(user_id, time_stamp);
        SELECT LAST_INSERT_ID() AS `vote_id`;
    ELSEIF (time_stamp < prev_time_stamp) THEN
        UPDATE Vote v
            SET v.time_stamp = time_stamp
            WHERE v.user_id = user_id;
        SET SQL_SAFE_UPDATES = 0;
        UPDATE Opt op
            INNER JOIN Choice c ON op.option_id = c.option_id
            SET op.total_votes_for = op.total_votes_for - 1
            WHERE c.vote_id = vote_id;
        SET SQL_SAFE_UPDATES = 1;
        DELETE FROM Choice c 
            WHERE c.vote_id = vote_id;
        SELECT vote_id;
    END IF;
END; //


/** 
 * Adds a choice to the casted vote.
 */
CREATE PROCEDURE AddChoice(
    IN vote_id INT,
    IN option_id INT)
BEGIN
    INSERT INTO Choice(vote_id, option_id)
    VALUES(vote_id, option_id);
    UPDATE Opt o
        SET o.total_votes_for = o.total_votes_for + 1
        WHERE o.option_id = option_id;
END; //


/**
 * Gets the voter_list for a particular election.
 */
CREATE PROCEDURE GetVoterList(
    IN election_id INT)
BEGIN
    SELECT u.user_id, u.voting_token, en.user_org_id FROM Election el
    INNER JOIN Enrollment en 
        ON el.org_id = en.org_id
    INNER JOIN Users u
        ON en.user_id = u.user_id
    WHERE el.election_id = election_id;
        
END; //



/** 
 * Gets all public elections. 
 */
CREATE PROCEDURE GetPublicElections()
BEGIN
    SELECT e.* FROM Election e
    WHERE e.public_results = TRUE;
END; //



/** A combined version of the first three functions,
    which was what was asked for on the queries document.
    In this, all the elections that the user is associated with
    are listed alongside the organization they belong to, as well
    as the election.*/
    CREATE PROCEDURE GetElectionsAlternate(IN id INT)
    BEGIN
        SELECT e.user_id, e.org_id, election_id, privilege, 
        start_time, end_time, verified, anonymous, public_results FROM Users u
        INNER JOIN Enrollment e
            ON e.user_id = u.user_id
        INNER JOIN Election el
            ON el.org_id = e.org_id
        WHERE e.user_id = id;
        
    END; //