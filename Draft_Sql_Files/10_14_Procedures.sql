USE voting_system;
DROP PROCEDURE IF EXISTS GetQuestionChoice; /** Tested */
DROP PROCEDURE IF EXISTS GetElectionQuestions; /** Tested */
DROP PROCEDURE IF EXISTS GetElectionListOrg; /** Tested */
DROP PROCEDURE IF EXISTS GetElection; /** Tested */

DROP PROCEDURE IF EXISTS UpdateElection; /** Tested*/
DROP PROCEDURE IF EXISTS DeleteElection; /** Tested*/
DROP PROCEDURE IF EXISTS CreateElection; /** Tested */

DROP PROCEDURE IF EXISTS AddQuestion; /** Tested */
DROP PROCEDURE IF EXISTS DropQuestion; /** Tested */
DROP PROCEDURE IF EXISTS UpdateQuestion; /** Tested*/

DROP PROCEDURE IF EXISTS AddChoice; /** Tested */
DROP PROCEDURE IF EXISTS DropChoice; /** May need to redesign.*/
DROP PROCEDURE IF EXISTS UpdateChoice; /** May need to double test this one. */
DROP PROCEDURE IF EXISTS GetQuestionSelection; /** Tested */

DELIMITER //

/** Gets all the potential answers to questions specified in
	param.*/
	
CREATE PROCEDURE GetQuestionChoice(
	IN id INT
	)
BEGIN
	SELECT * FROM Choice c
		INNER JOIN Question q
		ON c.question_id = q.question_id
	WHERE c.question_id = id;
END; //

/** Gets all of the questions from a specific election.*/

CREATE PROCEDURE GetElectionQuestions(
	IN id INT
	)
BEGIN
	SELECT q.question_id, q.election_id, q.description, q.selection_limit, q.is_required FROM Question q
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


/** Takes in several values as a parameter,
	then updates their corresponding fields.
	*/

CREATE PROCEDURE UpdateElection(
	IN id INT,
	IN description VARCHAR(40),
	IN verified BOOLEAN,
	IN start_time TIMESTAMP,
	IN end_time TIMESTAMP,
	IN is_anonymous BOOLEAN,
	IN is_public BOOLEAN
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


/** Takes in multiple values to create an election. */

CREATE PROCEDURE CreateElection(
	IN org_id INT,
	IN description VARCHAR(40),
	IN verified BOOLEAN,
	IN start_time TIMESTAMP,
	IN end_time TIMESTAMP,
	IN is_anonymous BOOLEAN,
	IN is_public BOOLEAN
	)
BEGIN
	INSERT INTO Election (org_id, description, verified, start_time, end_time,
							is_anonymous, is_public)
				VALUES(org_id, description, verified, start_time, end_time,
							is_anonymous, is_public);
END; //

/** Adds question to election. */

CREATE PROCEDURE AddQuestion(
	IN el_id INT,
	IN descr VARCHAR(40),
	IN sel INT,
	IN req TINYINT(1)
)
BEGIN
	INSERT INTO Question (election_id, description, selection_limit, is_required)
		VALUES (el_id, descr, sel, req);
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
	IN description VARCHAR(40),
	IN is_required TINYINT(1)
)
BEGIN

	UPDATE Question
		SET description = description
		WHERE question_id = id;
		
	UPDATE Question
		SET is_required = is_required
		WHERE question_id = id;
	
END; //

/** Adds a choice to a question. */

CREATE PROCEDURE AddChoice(
	IN id INT,
	IN descr VARCHAR(40)
)
BEGIN
	INSERT INTO Choice (question_id, description) 
	VALUES(id, descr);
	
	UPDATE Question
		SET selection_limit = selection_limit + 1
		WHERE question_id = id;
	
END; //

/** Drops a choice from a question. */

CREATE PROCEDURE DropChoice(
	IN id INT
)
BEGIN
	DELETE FROM Choice
	WHERE choice_id = id;
	
	UPDATE Question
		SET selection_limit = selection_limit - 1
		WHERE question_id = (SELECT question_id FROM Choice
			WHERE choice_id = id);
END; //

/** Updates choice for question.*/

CREATE PROCEDURE UpdateChoice(
	IN id INT,
	IN descr VARCHAR(40)
)
BEGIN
	UPDATE Question q
	SET description = descr
	WHERE question_id = id;
END; //

CREATE PROCEDURE GetQuestionSelection(
	IN id INT
)
BEGIN
	SELECT * FROM Choice
		WHERE question_id = id;
END; //



