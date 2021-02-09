DROP PROCEDURE IF EXISTS LoginUser;
DROP PROCEDURE IF EXISTS GetUser;
DROP PROCEDURE IF EXISTS GetUserToken;
DROP PROCEDURE IF EXISTS CreateUser;

DROP PROCEDURE IF EXISTS GetOrganizations;
DROP PROCEDURE IF EXISTS GetOrganization;
DROP PROCEDURE IF EXISTS CreateOrg;

DROP PROCEDURE IF EXISTS GetInvitedUsers;
DROP PROCEDURE IF EXISTS GetJoinedUsers;
DROP PROCEDURE IF EXISTS GetAllUsers;
DROP PROCEDURE IF EXISTS InviteUser;
DROP PROCEDURE IF EXISTS AcceptInvite;
DROP PROCEDURE IF EXISTS KickUser;
DROP PROCEDURE IF EXISTS UpdatePrivilege;

DROP PROCEDURE IF EXISTS GetRPIList;
DROP PROCEDURE IF EXISTS CreateRPI;
DROP PROCEDURE IF EXISTS AssignRPI;
DROP PROCEDURE IF EXISTS DeleteRPI;

DROP PROCEDURE IF EXISTS GetLocationList;
DROP PROCEDURE IF EXISTS CreateLocation;
DROP PROCEDURE IF EXISTS UpdateLocation;
DROP PROCEDURE IF EXISTS DeleteLocation;

DROP PROCEDURE IF EXISTS GetElectionListOrg;
DROP PROCEDURE IF EXISTS GetElectionListUser;
DROP PROCEDURE IF EXISTS GetElection;
DROP PROCEDURE IF EXISTS CreateElection;
DROP PROCEDURE IF EXISTS UpdateElection;
DROP PROCEDURE IF EXISTS DeleteElection;



DELIMITER //

/** 
	Takes in a user's login credentials,
	then returns the user's id
	*/

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
	SELECT user_id, first_name, last_name, email, date_of_birth FROM users
	WHERE user_id = id;
END; //





/** Takes in a user id, and returns the user's token
	(non-sensitive data). */
CREATE PROCEDURE GetUser(IN id INT)
BEGIN
	SELECT voting_token FROM users
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

	



/** Takes in a user's id, and returns the data of the organizations
	that the user specified belongs to.*/
CREATE PROCEDURE GetOrganizations(IN id INT)
BEGIN
	SELECT e.privilege_level, o.org_id, o.org_name FROM users u
		INNER JOIN enrollment e
			ON u.user_id = e.user_id
		INNER JOIN organization o
			ON e.org_id = o.org_id
	WHERE e.user_id = id;
END; //





/** Gets an organization's data from
	an organization id.*/
CREATE PROCEDURE GetOrganization(IN id INT)
BEGIN
	SELECT * FROM organization
	WHERE org_id = id;
END; //





/** Takes in a user id and a name for the organization,
	then uses this information to create an organization.*/
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




/** Takes in the id of an organization as a parameter, and
	displays all of the users who are currently in that organization.
	This includes their id, firstname, lastname, email, date_of_birth, and voting_token
	(I avoided any sensitive information such as their passwords of course).*/

CREATE PROCEDURE GetInvitedUsers(IN id INT)
BEGIN
	SELECT e.user_id, first_name, last_name, email, date_of_birth, voting_token, e.privilege FROM users
		INNER JOIN enrollment e
		   ON u.user_id = e.user_id
		INNER JOIN organization o
		   ON o.org_id = e.org_id
	WHERE o.org_id = id
	AND e.privilege_level = 0;
END; //




/** Takes in information, and uses it to create an election.*/
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

/** Takes in the id of a user and an organization, then 
	enrolls a user into an organization.*/
CREATE PROCEDURE EnrollUser(
	IN user_id INT, 
    IN org_id INT)
BEGIN
	INSERT INTO Enrollment(user_id, org_id)
	VALUES(user_id, org_id);
	SELECT LAST_INSERT_ID();
END; //


/** Takes in a user's id, and gets the elections 
    that are available to them.*/

CREATE PROCEDURE GetUserElections(IN id INT)
BEGIN
	SELECT election_id, el.org_id, start_time,
		end_time, status, is_anonymous FROM users u
			INNER JOIN enrollment e
				ON e.user_id = u.user_id
			INNER JOIN election el
				ON e.org_id = el.org_id	
	WHERE e.user_id = id;
END; //

/** A combined version of the first three functions,
	which was what was asked for on the queries document.
	In this, all the elections that the user is associated with
	are listed alongside the organization they belong to, as well
	as the election.*/
	CREATE PROCEDURE GetUserElectionsAlternate(IN id INT)
	BEGIN
		SELECT e.user_id, e.org_id, election_id, privilege_level, 
		start_time, end_time, status, is_anonymous FROM users u
		INNER JOIN enrollment e
			ON e.user_id = u.user_id
		INNER JOIN election el
			ON el.org_id = e.org_id
		WHERE e.user_id = id;
		
	END; //

FLUSH PRIVILEGES;



	