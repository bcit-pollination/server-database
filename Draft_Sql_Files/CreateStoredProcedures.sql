DROP PROCEDURE IF EXISTS GetUser;
DROP PROCEDURE IF EXISTS GetUserOrganization;
DROP PROCEDURE IF EXISTS GetUserElections;
DROP PROCEDURE IF EXISTS GetOrganizationUsers;
DROP PROCEDURE IF EXISTS GetUserElectionsAlternate;
DROP PROCEDURE IF EXISTS EnrollUser;
DROP PROCEDURE IF EXISTS CreateOrg;
DROP PROCEDURE IF EXISTS CreateUser;
DROP PROCEDURE IF EXISTS LoginUser;
DROP PROCEDURE IF EXISTS CreateElection;

DELIMITER //
CREATE PROCEDURE CreateElection(
	IN org_id INT, 
    IN description VARCHAR(40),
    IN start_time TIMESTAMP,
    IN end_time TIMESTAMP,
    IN is_anonymous BOOLEAN)
BEGIN
	INSERT INTO Election(org_id, description, start_time, end_time, is_anonymous)
    VALUES(org_id, description, start_time, end_time, is_anonymous);
	SELECT LAST_INSERT_ID();
END;//

CREATE PROCEDURE LoginUser(
	IN in_email VARCHAR(40),
    IN in_password VARCHAR(72))
BEGIN
	SELECT user_id FROM Users
    WHERE in_email = email 
    AND in_password = password;
END;//


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

CREATE PROCEDURE CreateOrg(
	IN user_id INT, 
    IN org_name VARCHAR(40))
BEGIN
	INSERT INTO Organization(org_name)
	VALUES(org_name);
	SELECT LAST_INSERT_ID();
	INSERT INTO Enrollment(user_id, org_id)
	VALUES(user_id, LAST_INSERT_ID());
END; //

CREATE PROCEDURE EnrollUser(
	IN user_id INT, 
    IN org_id INT)
BEGIN
	INSERT INTO Enrollment(user_id, org_id)
	VALUES(user_id, org_id);
	SELECT LAST_INSERT_ID();
END; //

/** Takes in a user id, and returns the user's data
	(non-sensitive data). */
DELIMITER //
CREATE PROCEDURE GetUser(IN id INT)
BEGIN
	SELECT user_id, first_name, last_name, email, date_of_birth, voting_token FROM users
	WHERE user_id = id;
END //
DELIMITER ;

/** Takes in a user's id, and returns the data of the organizations
	that the user specified belongs to.*/
DELIMITER //
CREATE PROCEDURE GetUserOrganization(IN id INT)
BEGIN
	SELECT o.org_id, o.org_name, e.privilege_level FROM users u
		INNER JOIN enrollment e
			ON u.user_id = e.user_id
		INNER JOIN organization o
			ON e.org_id = o.org_id
	WHERE e.user_id = id;
END //
DELIMITER ;

/** Takes in a user's id, and gets the elections 
    that are available to them.*/
DELIMITER //
CREATE PROCEDURE GetUserElections(IN id INT)
BEGIN
	SELECT election_id, el.org_id, start_time,
		end_time, status, is_anonymous FROM users u
			INNER JOIN enrollment e
				ON e.user_id = u.user_id
			INNER JOIN election el
				ON e.org_id = el.org_id	
	WHERE e.user_id = id;
END //
DELIMITER ;


/** Takes in the id of an organization as a parameter, and
	displays all of the users who are currently in that organization.
	This includes their id, firstname, lastname, email, date_of_birth, and voting_token
	(I avoided any sensitive information such as their passwords of course).*/
DELIMITER //
CREATE PROCEDURE GetOrganizationUsers(IN id INT)
BEGIN
	SELECT e.user_id, first_name, last_name, email, date_of_birth, voting_token FROM users
		INNER JOIN enrollment e
		   ON u.user_id = e.user_id
		INNER JOIN organization o
		   ON o.org_id = e.org_id
	WHERE o.org_id = id;
END //
DELIMITER ;

/** A combined version of the first three functions,
	which was what was asked for on the queries document.
	In this, all the elections that the user is associated with
	are listed alongside the organization they belong to, as well
	as the election.*/
		DELIMITER //
	CREATE PROCEDURE GetUserElectionsAlternate(IN id INT)
	BEGIN
		SELECT e.user_id, e.org_id, election_id, privilege_level, 
		start_time, end_time, status, is_anonymous FROM users u
		INNER JOIN enrollment e
			ON e.user_id = u.user_id
		INNER JOIN election el
			ON el.org_id = e.org_id
		WHERE e.user_id = id;
		
	END //
	DELIMITER ;	

GRANT EXECUTE ON PROCEDURE GetUser TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE GetUserOrganization TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE GetUserElections TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE GetOrganizationUsers TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE GetUserElectionsAlternate TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE CreateOrg TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE CreateUser TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE EnrollUser TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE LoginUser TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE CreateElection TO 'server'@'localhost';

FLUSH PRIVILEGES;



	