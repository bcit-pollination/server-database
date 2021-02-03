DROP PROCEDURE IF EXISTS get_user_info;
DROP PROCEDURE IF EXISTS create_user;
DROP PROCEDURE IF EXISTS update_user_fname;
DROP PROCEDURE IF EXISTS update_user_lname;

/** WILL WE NEED TO ADD EMAIL, PASSWORD*/

/** Gets all (non sensitive) user info from token. */
DELIMITER //
CREATE PROCEDURE get_user_info(
   IN id_val VARCHAR(36)
)
BEGIN
	SELECT first_name, last_name FROM users
    WHERE voting_token = id_val;
END //
DELIMITER ;

/** Allows user to securely create a user with a randomized uuid. */
DELIMITER //
CREATE PROCEDURE create_user(IN fname VARCHAR(40), IN lname VARCHAR(40), IN uuid VARCHAR(36))
BEGIN
	INSERT INTO users (first_name, last_name, voting_token)
        VALUES (fname, lname, uuid);
END //
DELIMITER ;

/** Updates a user's first name. */
DELIMITER //
CREATE PROCEDURE update_user_fname(IN fname VARCHAR(40), IN id_val VARCHAR(36))
BEGIN
	UPDATE users
    SET first_name = fname
    WHERE voting_token = id_val;
END //
DELIMITER ;

/** Updates a user's last name. */
DELIMITER //
CREATE PROCEDURE update_user_lname(IN lname VARCHAR(40), IN id_val VARCHAR(36))
BEGIN
	UPDATE users
    SET last_name = lname
    WHERE voting_token = id_val;
END //
DELIMITER ;

/** Gets organization information. */

DELIMITER //
CREATE PROCEDURE get_org_info(IN id_val VARCHAR(36))
BEGIN
	
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE create_org()
BEGIN

END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE update_org_info()
BEGIN

END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE delete_org_name()
BEGIN

END //
DELIMITER ;
