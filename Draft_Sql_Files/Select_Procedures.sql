DROP PROCEDURE IF EXISTS get_user;
DROP PROCEDURE IF EXISTS get_user_organization;
DROP PROCEDURE IF EXISTS get_user_elections;
DROP PROCEDURE IF EXISTS get_organization_users;

/** Gets user data from the user's id. */
DELIMITER //
CREATE get_user(IN id INT)
BEGIN
	SELECT first_name, last_name, voting_token FROM users
	WHERE user_id = id;
END //
DELIMITER ;

/** Gets the data from the organizations that the user
	belongs to from the user's id. */
DELIMITER //
CREATE get_user_organization(IN id INT)
BEGIN
	SELECT first_name, last_name, voting_token FROM users
	WHERE user_id = id;
END //
DELIMITER ;

/** Gets the elections that are available to user.*/
DELIMITER //
CREATE get_user_organization(IN id INT)
BEGIN
	SELECT first_name, last_name, voting_token FROM users
	WHERE user_id = id;
END //
DELIMITER ;
