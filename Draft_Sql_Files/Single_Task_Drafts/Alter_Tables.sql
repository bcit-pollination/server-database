USE voting_system;
/** This script is to alter the Choice table, and turn it into
the Opt table. This will also turn the Selection table to the
Choice table. The fields of these tables will be renamed accordingly,
in addition to the procedures that use said fields. */

DROP PROCEDURE IF EXISTS CreateVote;
DROP PROCEDURE IF EXISTS CreateSelection;
DROP PROCEDURE IF EXISTS GetVoteResults;
DROP PROCEDURE IF EXISTS GetQuestionChoice;
DROP PROCEDURE IF EXISTS AddChoice;
DROP PROCEDURE IF EXISTS DropChoice;
DROP PROCEDURE IF EXISTS UpdateChoice;
DROP PROCEDURE IF EXISTS GetQuestionSelection;
DROP PROCEDURE IF EXISTS GetElectionQuestions;
DROP PROCEDURE IF EXISTS AddQuestion;

DROP PROCEDURE IF EXISTS CreateChoice; /** CreateSelection */
DROP PROCEDURE IF EXISTS GetQuestionOpt; /** GetQuestionChoice */
DROP PROCEDURE IF EXISTS AddOpt; /** AddChoice */
DROP PROCEDURE IF EXISTS DropOpt; /** DropChoice */
DROP PROCEDURE IF EXISTS UpdateOpt; /** UpdateChoice */
DROP PROCEDURE IF EXISTS GetQuestionChoice; /** GetQuestionSelection */

/** Rename Tables */

ALTER TABLE Question
RENAME COLUMN selection_limit TO opt_limit;

ALTER TABLE Choice
RENAME TO Opt;

ALTER TABLE Opt
RENAME COLUMN choice_id TO opt_id;

ALTER TABLE Selection
RENAME TO Choice;

ALTER TABLE Choice
RENAME COLUMN choice_id TO opt_id;

ALTER TABLE Choice
RENAME COLUMN selection_id TO choice_id;

/** ---------------------------------- */


DELIMITER //

/** Adds a vote. */
CREATE PROCEDURE CreateVote(
	IN voting_token VARCHAR(36),
    IN time_stamp TIMESTAMP,
    IN election_id INT
)
BEGIN
	DECLARE var_user_id INT;
    DECLARE previous_vote INT;

    SET var_user_id = (
		SELECT user_id 
        FROM Users u
        WHERE u.voting_token = voting_token
	);
    SET previous_vote = (
		SELECT v.vote_id FROM Election el
			INNER JOIN Question q
				ON el.election_id = q.election_id
			INNER JOIN Opt c
				ON c.question_id = c.question_id
			INNER JOIN Choice s
				ON s.opt_id = c.opt_id
			INNER JOIN Vote v
				ON v.vote_id = s.vote_id
	);
    
    IF (COUNT(previous_vote) > 0) THEN
		IF (time_stamp > previous_vote) THEN
			INSERT INTO Vote(user_id, time_stamp)
            VALUES(var_user_id, time_stamp);
            SELECT LAST_INSERT_ID();
        END IF;
	ELSE
		INSERT INTO Vote(user_id, time_stamp)
		VALUES(var_user_id, time_stamp);
		SELECT LAST_INSERT_ID();
    END IF;
END; //

/** Adds a selection. */
CREATE PROCEDURE CreateChoice(
	IN voting_token VARCHAR(36),
    IN opt_id INT
)
BEGIN
	DECLARE var_user_id INT;
    SET var_user_id = (
		SELECT user_id 
        FROM Users u
        WHERE u.voting_token = voting_token
	);
	INSERT INTO Choice(var_user_id, opt_id)
	VALUES(var_user_id, opt_id);
END; //

/** Gets votes with selected choices for questions for a particular election. */
CREATE PROCEDURE GetVoteResults(
	IN election_id INT
)
BEGIN
	SELECT v.vote_id, s.*, c.*, q.question_id, q.description FROM Election el
		INNER JOIN Question q
			ON el.election_id = q.election_id
		INNER JOIN Opt c
			ON c.question_id = c.question_id
		INNER JOIN Choice s
			ON s.opt_id = c.opt_id
		INNER JOIN Vote v
			ON v.vote_id = s.vote_id;
END; //

/** Gets all the potential answers to questions specified in
	param.*/
	
CREATE PROCEDURE GetQuestionOpt(
	IN id INT
	)
BEGIN
	SELECT * FROM Opt c
		INNER JOIN Question q
		ON c.question_id = q.question_id
	WHERE c.question_id = id;
END; //

/** Adds question to election. */

CREATE PROCEDURE AddQuestion(
	IN el_id INT,
	IN descr VARCHAR(40),
	IN sel INT,
	IN req TINYINT(1)
)
BEGIN
	INSERT INTO Question (election_id, description, opt_limit, is_required)
		VALUES (el_id, descr, sel, req);
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
		SET opt_limit = opt_limit + 1
		WHERE question_id = id;
	
END; //

/** Drops a choice from a question. */

CREATE PROCEDURE DropOpt(
	IN id INT
)
BEGIN

	UPDATE Question q
	INNER JOIN Opt c ON q.question_id = c.question_id
	SET opt_limit = opt_limit - 1
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

CREATE PROCEDURE GetQuestionChoice(
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
	SELECT q.question_id, q.election_id, q.description, q.opt_limit, q.is_required FROM Question q
		INNER JOIN Election el
		ON el.election_id = q.election_id
		WHERE q.election_id = id;
END; //