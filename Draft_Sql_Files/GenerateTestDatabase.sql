/**
 * Populates a test database using stored procedures.
 * Prerequisite:
 * 1) Run SetUpDatabase.sql
 * 2) Run CreateStoredProcedures.sql
 */
USE voting_system;

CALL CreateUser("Albert", "W", "albertw777@gmail.com", "1985-01-01", "2510", "123");
CALL CreateUser("Bruce", "L", "brucel23@gmail.com", "1981-01-01", "1510", "456");
CALL CreateUser("Arron", "F", "arronf17@gmail.com", "1982-01-01", "1537", "789");

CALL CreateOrg(1, "COMP2510 Study Group", "password1", "pw1"); /* Albert */
CALL CreateOrg(3, "COMP1537 Discord", "password2", "pw2"); /* Arron */

CALL InviteUser("albertw777@gmail.com", "userorgid1", 2); /* Albert is invited to COMP1537 Discord */
CALL InviteUser("brucel23@gmail.com", "userorgid2", 2); /* Bruce is invited to COMP1537 Discord */

CALL UpdatePrivilege(2, 2, 1); /* Bruce is promoted to member */

CALL CreateElection(2, "Web Dev", CURRENT_TIMESTAMP(), TIMESTAMPADD(hour, 1, CURRENT_TIMESTAMP()), TRUE, TRUE, TRUE); /** Creates an Election for COMP1537 Discord*/
CALL CreateElection(1, "C Survey", CURRENT_TIMESTAMP(), TIMESTAMPADD(hour, 1, CURRENT_TIMESTAMP()), TRUE, FALSE, FALSE); /** Creates an Election for COMP2510 Study Group*/

CALL AddQuestion(1, 'Where did you go to school?', 1, 4, TRUE); /** Adds new question to our first election. */

CALL AddOption(1, 'Javascript'); /** First option is added. */
CALL AddOption(1, 'CSS'); /** Second option is added. */
CALL AddOption(1, 'HTML'); /** Third option is added. */
CALL AddOption(1, 'Python'); /** Third option is added. */

CALL AddQuestion(2, 'Where did you go to school?', 1, 1, FALSE); /** Adds new question to our second election. */

CALL AddOption(2, 'BCIT'); /** First option is added. */
CALL AddOption(2, 'UBC'); /** Second option is added. */
CALL AddOption(2, 'SFU'); /** Third option is added. */

CALL UpdateOption(2, 'PHP'); /** Changes option 'CSS' to 'PHP'*/
CALL UpdateQuestion(1, 'What language do you like?', 1, 3, FALSE); /** Changes the question. */
CALL UpdateElection(1, 'Web Dev Survey', '2021-10-05', '2021-11-09', TRUE, FALSE, FALSE); /** Updates election name to web dev survey. */

CALL UpdateUser(1, "password");
CALL DeactivateUser(2);
CALL UpdatePrivilege(2, 2, 0);
CALL UpdateOrg(1, "This is an org name", "verifier password");

CALL AddVote('123', '2028-01-04 01:01:04', 1);
CALL AddChoice(1, 1, 1);
CALL AddChoice(1, 2, 2);

CALL AddVote('456', '2028-01-04 01:01:04', 1);
CALL AddChoice(2, 1, 1);
CALL AddChoice(2, 2, 2);

CALL AddVote('789', '2028-01-04 01:01:04', 1);
CALL AddChoice(3, 1, 1);
CALL AddChoice(3, 2, 2);

CALL AddVote('123', '2028-01-04 01:01:01', 2);
CALL AddChoice(4, 5, 1);
CALL AddChoice(4, 6, 2);

CALL UpdateVerifierPassword(1, "Hello world");
CALL UpdateUserOrgId(1, 1, "Passport");

CALL GetPublicElections(5,2);
/* CALL DeleteQuestion(1); */
/* CALL DeleteOption(1); */