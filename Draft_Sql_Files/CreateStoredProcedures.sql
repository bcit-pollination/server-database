USE voting_system;

DROP PROCEDURE IF EXISTS LoginUser;
DROP PROCEDURE IF EXISTS GetUser;
DROP PROCEDURE IF EXISTS GetUserToken;
DROP PROCEDURE IF EXISTS CreateUser;
DROP PROCEDURE IF EXISTS UpdateUser;
DROP PROCEDURE IF EXISTS DeactivateUser;

DROP PROCEDURE IF EXISTS GetOrganizations;
DROP PROCEDURE IF EXISTS GetOrganization;
DROP PROCEDURE IF EXISTS CreateOrg;
DROP PROCEDURE IF EXISTS UpdateOrg;
DROP PROCEDURE IF EXISTS DisbandOrg;
DROP PROCEDURE IF EXISTS GetVerifierPassword;

DROP PROCEDURE IF EXISTS GetUsersFromOrg;
DROP PROCEDURE IF EXISTS InviteUser;
DROP PROCEDURE IF EXISTS UpdatePrivilege;

DROP PROCEDURE IF EXISTS GetLocationList;
DROP PROCEDURE IF EXISTS CreateLocation;
DROP PROCEDURE IF EXISTS UpdateLocation;
DROP PROCEDURE IF EXISTS DeleteLocation;

DROP PROCEDURE IF EXISTS GetElectionListOrg; /** Tested */
DROP PROCEDURE IF EXISTS GetElectionListUser;
DROP PROCEDURE IF EXISTS GetElection; /** Tested */
DROP PROCEDURE IF EXISTS UpdateElection; /** Tested*/
DROP PROCEDURE IF EXISTS DeleteElection; /** Tested*/
DROP PROCEDURE IF EXISTS CreateElection; /** Tested */

DROP PROCEDURE IF EXISTS CreateVote;
DROP PROCEDURE IF EXISTS CreateChoice;
DROP PROCEDURE IF EXISTS GetVoteResults;
DROP PROCEDURE IF EXISTS GetIndividualVotes;

DROP PROCEDURE IF EXISTS GetPublicElectionList;

DROP PROCEDURE IF EXISTS GetElectionsAlternate;

DROP PROCEDURE IF EXISTS GetQuestionOpt; /** Tested */
DROP PROCEDURE IF EXISTS GetElectionQuestions; /** Tested */
DROP PROCEDURE IF EXISTS GetPublicElections;

DROP PROCEDURE IF EXISTS AddQuestion; /** Tested */
DROP PROCEDURE IF EXISTS DropQuestion; /** Tested */
DROP PROCEDURE IF EXISTS UpdateQuestion; /** Tested*/

DROP PROCEDURE IF EXISTS AddOpt; /** Tested */
DROP PROCEDURE IF EXISTS DropOpt; /** Tested*/
DROP PROCEDURE IF EXISTS UpdateOpt; /** Tested. */

DROP PROCEDURE IF EXISTS GetPrivilege;
DROP PROCEDURE IF EXISTS GetIdVt; /** Tested */

DELIMITER //

/** Takes in a user's login credentials,
	then returns the user's id. */
CREATE PROCEDURE LoginUser(
	IN in_email VARCHAR(40),
    IN in_password VARCHAR(72))
BEGIN
	SELECT user_id FROM Users
    WHERE in_email = email 
    AND in_password = password;
END;//


/** Takes in a user id, and returns the user's data
	(non-sensitive data). */
CREATE PROCEDURE GetUser(IN id INT)
BEGIN
	SELECT user_id, first_name, last_name, email, date_of_birth FROM Users
	WHERE user_id = id;
END; //


/** Takes in a user id, and returns the user's token
	(non-sensitive data). */
CREATE PROCEDURE GetUserToken(IN id INT)
BEGIN
	SELECT voting_token FROM Users
	WHERE user_id = id;
END; //


/** Takes in user information, and uses it
	to create a user. */
CREATE PROCEDURE CreateUser(
	IN first_name VARCHAR(40), 
    IN last_name VARCHAR(40), 
    IN email VARCHAR(40),
    IN date_of_birth DATE,
    IN password VARCHAR(40),
    IN voting_token VARCHAR(36))
BEGIN
	INSERT INTO Users(first_name, last_name, email, date_of_birth, 
		password, voting_token)
	VALUES(first_name, last_name, email, date_of_birth, 
		password, voting_token);
	SELECT LAST_INSERT_ID();
END; //


/** Changes user password given the specified user_id. */
CREATE PROCEDURE UpdateUser(
	IN in_user_id INT,
    IN in_password VARCHAR(72)
)
BEGIN
	UPDATE Users
    SET password = in_password
	WHERE user_id = in_user_id;
END; //


/* Deactivates a user by setting the user's disabled flag. */
CREATE PROCEDURE DeactivateUser(IN id INT)
BEGIN
	UPDATE Users
    SET disabled = TRUE
	WHERE user_id = id;
END; //

	
/** Takes in a user's id, and returns the data of the organizations
	that the user specified belongs to.*/
CREATE PROCEDURE GetOrganizations(IN id INT)
BEGIN
	SELECT e.privilege_level, o.org_id, o.org_name FROM Users u
		INNER JOIN Enrollment e
			ON u.user_id = e.user_id
		INNER JOIN Organization o
			ON e.org_id = o.org_id
	WHERE e.user_id = id;
END; //


/** Gets an organization's data from
	an organization id.*/
CREATE PROCEDURE GetOrganization(IN id INT)
BEGIN
	SELECT org_id, org_name FROM Organization
	WHERE org_id = id;
END; //


/** Takes in a user id and a name for the organization,
	then uses this information to create an organization.*/
CREATE PROCEDURE CreateOrg(
	IN user_id INT, 
    IN org_name VARCHAR(40),
    IN verifier_password VARCHAR(72))
BEGIN
	INSERT INTO Organization(org_name, verifier_password)
	VALUES(org_name, verifier_password);
	SELECT LAST_INSERT_ID();
	INSERT INTO Enrollment(user_id, org_id)
	VALUES(user_id, LAST_INSERT_ID());
END; //


/** Updates an organization's password and name. **/
CREATE PROCEDURE UpdateOrg(
	IN in_org_id INT, 
    IN in_org_name VARCHAR(40),
    IN in_verifier_password VARCHAR(72))
BEGIN
	UPDATE Organization
    SET verifier_password = in_verifier_password,
    org_name = in_org_name
	WHERE org_id = in_org_id;
END; //


/** Disbands an organization by setting its disabled flag and the enrollment disabled flags. */
CREATE PROCEDURE DisbandOrg(IN in_org_id INT)
BEGIN
	UPDATE Organization
    SET disabled = TRUE
	WHERE org_id = in_org_id;
	UPDATE Enrollment
    SET disabled = TRUE
	WHERE org_id = in_org_id;
END; //


/** Gets the verifier password for the specified organization. */
CREATE PROCEDURE GetVerifierPassword(IN in_org_id INT)
BEGIN
	SELECT verifier_password FROM Organization
	WHERE org_id = in_org_id;
END; //

 
/** Takes in the id of an organization and the privilege level as parameters, and
	displays all of the users who are currently in that organization.
	This includes their id, firstname, lastname, email, date_of_birth, and voting_token
	(I avoided any sensitive information such as their passwords of course).*/

CREATE PROCEDURE GetUsersFromOrg(IN id INT, IN privilege_level INT)
BEGIN
	SELECT e.user_id, first_name, last_name, email, date_of_birth, voting_token, e.privilege FROM Users
		INNER JOIN Enrollment e
		   ON u.user_id = e.user_id
		INNER JOIN Organization o
		   ON o.org_id = e.org_id
	WHERE o.org_id = id
	AND e.privilege_level = privelege_level;
END; //


/** Updates the prvilege level for a user. */
CREATE PROCEDURE UpdatePrivilege(
	IN in_user_id INT,
	IN in_org_id INT,
    IN in_privilege_level INT
)
BEGIN
	UPDATE Enrollment
    SET privilege_level = in_privilege_level
	WHERE user_id = in_user_id
    AND org_id = in_org_id;
END; //


/** Takes in the id of a user and an organization, then 
	invites a user into an organization.*/
CREATE PROCEDURE InviteUser(
	IN user_id INT, 
    IN org_id INT)
BEGIN
	INSERT INTO Enrollment(user_id, org_id)
	VALUES(user_id, org_id);
	SELECT LAST_INSERT_ID();
END; //


/** Takes in information, and uses it to create an election.*/
CREATE PROCEDURE CreateElection(
	IN org_id INT, 
    IN description VARCHAR(40),
    IN start_time TIMESTAMP,
    IN end_time TIMESTAMP,
	IN is_anonymous BOOLEAN,
	IN is_public BOOLEAN,
    IN verified BOOLEAN)
BEGIN
	INSERT INTO Election(org_id, description, start_time, end_time, is_anonymous, is_public)
    VALUES(org_id, description, start_time, end_time, is_anonymous, is_public);
	SELECT LAST_INSERT_ID();
END;//


/** Takes in a user's id, and gets the elections 
    that are available to them.*/

CREATE PROCEDURE GetElectionListUser(IN id INT)
BEGIN
	SELECT election_id, el.org_id, start_time,
		end_time, verified, is_anonymous, is_public FROM Users u
			INNER JOIN Enrollment e
				ON e.user_id = u.user_id
			INNER JOIN Election el
				ON e.org_id = el.org_id	
	WHERE e.user_id = id;
END; //

/** Adds a vote, getting the ID if successfully added or updated.
    Previously selected choices are deleted if vote was updated. */
CREATE PROCEDURE CreateVote(
	IN voting_token VARCHAR(36),
    IN time_stamp TIMESTAMP,
    IN election_id INT
)
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
		SELECT LAST_INSERT_ID();
    ELSEIF (time_stamp < prev_time_stamp) THEN
		UPDATE Vote v
			SET v.time_stamp = time_stamp
			WHERE v.user_id = user_id;
		SET SQL_SAFE_UPDATES = 0;
		UPDATE Opt op
			INNER JOIN Choice c ON op.opt_id = c.opt_id
			SET op.total_choices = op.total_choices - 1
            WHERE c.vote_id = vote_id;
		SET SQL_SAFE_UPDATES = 1;
        DELETE FROM Choice c 
			WHERE c.vote_id = vote_id;
        SELECT vote_id;
    END IF;
END; //


/** Adds a choice. */
CREATE PROCEDURE CreateChoice(
	IN vote_id INT,
    IN opt_id INT
)
BEGIN
	INSERT INTO Choice(vote_id, opt_id)
	VALUES(vote_id, opt_id);
    UPDATE Opt o
		SET o.total_choices = o.total_choices + 1
        WHERE o.opt_id = opt_id;
END; //


/** Gets votes of each user for a particular election. */
CREATE PROCEDURE GetIndividualVotes(
	IN election_id INT
)
BEGIN   
	SELECT u.first_name, u.last_name, q.question_id, q.description AS `Question Description`, o.opt_id, o.description AS `Option Description` FROM Election el
		INNER JOIN Question q
			ON el.election_id = q.election_id
		INNER JOIN Opt o
			ON q.question_id = o.question_id
		INNER JOIN Choice c
			ON o.opt_id = c.opt_id
		INNER JOIN Vote v
			ON c.vote_id = v.vote_id
		INNER JOIN Users u
			ON v.user_id = u.user_id;
END; //




/** A combined version of the first three functions,
	which was what was asked for on the queries document.
	In this, all the elections that the user is associated with
	are listed alongside the organization they belong to, as well
	as the election.*/
	CREATE PROCEDURE GetElectionsAlternate(IN id INT)
	BEGIN
		SELECT e.user_id, e.org_id, election_id, privilege_level, 
		start_time, end_time, verified, is_anonymous, is_public FROM Users u
		INNER JOIN Enrollment e
			ON e.user_id = u.user_id
		INNER JOIN Election el
			ON el.org_id = e.org_id
		WHERE e.user_id = id;
		
	END; //
	
/** Gets all the potential answers to questions specified in
	param.*/
	
CREATE PROCEDURE GetQuestionOpt(
	IN id INT
)
BEGIN
	SELECT * FROM Opt
		WHERE question_id = id;
END; //

/** Gets all of the questions from a specific election.*/

CREATE PROCEDURE GetElectionQuestions(
	IN id INT
	)
BEGIN
	SELECT q.* FROM Question q
		INNER JOIN Election el
		ON el.election_id = q.election_id
		WHERE q.election_id = id;
END; //

/** Gets elections from an organization id. */

CREATE PROCEDURE GetElectionListOrg(
	IN id INT
	)
BEGIN
	SELECT * FROM Election
		WHERE org_id = id;
END; //

/** Gets an election from an election id. */

CREATE PROCEDURE GetElection(
	IN id INT
	)
BEGIN
	SELECT * FROM Election
		WHERE election_id = id;
END; //

/** Gets all elections if they are open to public. */

CREATE PROCEDURE GetPublicElections()
BEGIN
	SELECT * FROM Election
    WHERE is_public = TRUE;
END; //


/** Takes in several values as a parameter,
	then updates their corresponding fields.
	*/

CREATE PROCEDURE UpdateElection(
	IN id INT,
	IN description VARCHAR(40),
	IN start_time TIMESTAMP,
	IN end_time TIMESTAMP,
	IN is_anonymous BOOLEAN,
	IN is_public BOOLEAN,
    IN verified BOOLEAN
	)
BEGIN
	UPDATE Election
		SET description = description
		WHERE election_id = id;
		
	UPDATE Election
		SET verified = verified
		WHERE election_id = id;
	
	UPDATE Election
		SET start_time = start_time
		WHERE election_id = id;
		
	UPDATE Election
		SET end_time = end_time
		WHERE election_id = id;
		
	UPDATE Election
		SET is_anonymous = is_anonymous
		WHERE election_id = id;
		
	UPDATE Election
		SET is_public = is_public
		WHERE election_id = id;
END; //

/** Takes in an election's id, and deletes the election
	attached to it.*/

CREATE PROCEDURE DeleteElection(
	IN id INT
	)
BEGIN
	DELETE FROM Election
	WHERE election_id = id;
END; //

/** Adds question to election. */

CREATE PROCEDURE AddQuestion(
	IN election_id INT,
	IN description VARCHAR(40),
	IN choice_limit INT
)
BEGIN
	INSERT INTO Question (election_id, description, choice_limit)
		VALUES (election_id, description, choice_limit);
END; //

/** Drops Question from an election. */

CREATE PROCEDURE DropQuestion(
	IN id INT
)
BEGIN
	DELETE FROM Question
	WHERE question_id = id;
END; //

/** Updates a question. */

CREATE PROCEDURE UpdateQuestion(
	IN id INT,
	IN description VARCHAR(40)
)
BEGIN

	UPDATE Question
		SET description = description
		WHERE question_id = id;
END; //

/** Adds a choice to a question. */

CREATE PROCEDURE AddOpt(
	IN id INT,
	IN descr VARCHAR(40)
)
BEGIN
	INSERT INTO Opt (question_id, description) 
	VALUES(id, descr);
	
	UPDATE Question
		SET choice_limit = choice_limit + 1
		WHERE question_id = id;
	
END; //

/** Drops a choice from a question. */

CREATE PROCEDURE DropOpt(
	IN id INT
)
BEGIN

	UPDATE Question q
	INNER JOIN Opt c ON q.question_id = c.question_id
	SET choice_limit = choice_limit - 1
	WHERE c.opt_id = id;
	
	DELETE FROM Opt
	WHERE opt_id = id; 
	
END; //

/** Updates choice for question.*/

CREATE PROCEDURE UpdateOpt(
	IN id INT,
	IN descr VARCHAR(40)
)
BEGIN
	UPDATE Opt
	SET description = descr
	WHERE opt_id = id;
END; //

/** Gets the privilege_level of a particular user
 from a particular organization*/

CREATE PROCEDURE GetPrivilege(
	IN org_id INT,
	IN user_id INT
)
BEGIN
	SELECT privilege_level FROM Enrollment
	WHERE org_id = org_id
	AND user_id = user_id;
END; //

CREATE PROCEDURE GetIdVt(
	IN election_id INT
)
BEGIN
	SELECT u.user_id, u.voting_token, en.identification FROM Election el
    INNER JOIN Enrollment en 
		ON el.org_id = en.org_id
    INNER JOIN Users u
		ON en.user_id = u.user_id
	WHERE el.election_id = election_id;
        
END; //

	