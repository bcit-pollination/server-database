USE voting_system;

DROP PROCEDURE IF EXISTS GetPublicElections;

DELIMITER //

CREATE PROCEDURE GetPublicElections()
BEGIN
	SELECT * FROM Election
    WHERE is_public = TRUE;
END; //