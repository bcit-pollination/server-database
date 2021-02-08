INSERT INTO users (first_name, last_name, email, DOB, password_salt, password_hash, voting_token)
       VALUES ('test', 'test', 'test', '2001-09-18', 'test', 'test', 'test');
       
INSERT INTO users (first_name, last_name, email, DOB, password_salt, password_hash, voting_token)
       VALUES ('test1', 'test1', 'test1', '2004-10-10', 'test1', 'test1', 'test1');
	   
INSERT INTO organization (org_name)
	VALUE ('Random Org');

INSERT INTO enrollment (user_id, org_id, privilege_level, identification)
	VALUE (1, 1, 1, 'Card');
	
INSERT INTO enrollment (user_id, org_id, privilege_level, identification)	
	VALUE (2, 1, 1, 'Card');
	
INSERT INTO election (org_id, status, is_anonymous)
	VALUE (1, 'PUBLISHED', 1);
	
/** CALL get_user(1); */

/** CALL get_user_organization(1); */

/** CALL get_user_elections(1); */

/** CALL get_user_elections(1); */

/** CALL get_organization_users(1); */

/** CALL get_user_elections_alternate(1); */