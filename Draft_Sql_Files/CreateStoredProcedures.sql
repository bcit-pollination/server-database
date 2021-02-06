DROP PROCEDURE IF EXISTS get_user;
DROP PROCEDURE IF EXISTS get_user_organization;
DROP PROCEDURE IF EXISTS get_user_elections;
DROP PROCEDURE IF EXISTS get_organization_users;
DROP PROCEDURE IF EXISTS get_user_elections_alternate;
/**DROP PROCEDURE IF EXISTS RegisterUser; */
DROP PROCEDURE IF EXISTS CreateOrg;
DROP PROCEDURE IF EXISTS CreateUser;

DELIMITER //
CREATE PROCEDURE CreateUser(
	IN first_name VARCHAR(40), 
    IN last_name VARCHAR(40), 
    IN email VARCHAR(40),
    IN DOB DATE,
    IN password_salt VARCHAR(40),
    IN password_hash VARCHAR(40),
    IN voting_token VARCHAR(36))
BEGIN
  INSERT INTO Users(first_name, last_name, email, DOB, 
	password_salt, password_hash, voting_token)
  VALUES(first_name, last_name, email, DOB, 
	password_salt, password_hash, voting_token);
END; //

CREATE PROCEDURE CreateOrg(
	IN user_id INT, 
    IN org_name VARCHAR(40))
BEGIN
  INSERT INTO Organization(org_name)
  VALUES(org_name);
  INSERT INTO Enrollment(user_id, org_id)
  VALUES(user_id, LAST_INSERT_ID());
END; //

CREATE PROCEDURE EnrollUser(
	IN user_id INT, 
    IN org_id INT)
BEGIN
  INSERT INTO Enrollment(user_id, org_id)
  VALUES(user_id, org_id);
END; //

/** Takes in a user id, and returns the user's data
	(non-sensitive data). */
DELIMITER //
CREATE PROCEDURE get_user(IN id INT)
BEGIN
	SELECT user_id, first_name, last_name, email, DOB, voting_token FROM users
	WHERE user_id = id;
END //
DELIMITER ;

/** Takes in a user's id, and returns the data of the organizations
	that the user specified belongs to.*/
DELIMITER //
CREATE PROCEDURE get_user_organization(IN id INT)
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
CREATE PROCEDURE get_user_elections(IN id INT)
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
	This includes their id, firstname, lastname, email, DOB, and voting_token
	(I avoided any sensitive information such as their passwords of course).*/
DELIMITER //
CREATE PROCEDURE get_organization_users(IN id INT)
BEGIN
	SELECT e.user_id, first_name, last_name, email, DOB, voting_token FROM users u
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
	CREATE PROCEDURE get_user_elections_alternate(IN id INT)
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

GRANT EXECUTE ON PROCEDURE get_user TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE get_user_organization TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE get_user_elections TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE get_organization_users TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE get_user_elections_alternate TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE CreateOrg TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE CreateUser TO 'server'@'localhost';
GRANT EXECUTE ON PROCEDURE EnrollUser TO 'server'@'localhost';

FLUSH PRIVILEGES;



	