/**
 * Populates a test database using stored procedures.
 * Prerequisite:
 * 1) Run SetUpDatabase.sql
 * 2) Run CreateStoredProcedures.sql
 */
USE voting_system;

CALL CreateUser("Albert", "W", "albertw777@gmail.com", "1985-01-01", "2510", "A01287456");
CALL CreateUser("Bruce", "L", "brucel23@gmail.com", "1981-01-01", "1510", "A01287745");
CALL CreateUser("Arron", "F", "arronf17@gmail.com", "1982-01-01", "1537", "A02807121");

CALL CreateOrg(1, "COMP2510 Study Group", "password1"); /* Albert */
CALL CreateOrg(3, "COMP1537 Discord", "password2"); /* Arron */

CALL InviteUser(1, 2); /* Albert is invited to COMP1537 Discord */
CALL InviteUser(2, 2); /* Bruce is invited to COMP1537 Discord */

CALL UpdatePrivilege(1, 2, 2); /* Albert is promoted to admin */
CALL UpdatePrivilege(2, 2, 1); /* Bruce is promoted to member */

CALL CreateElection(2, "Web Dev", CURRENT_TIMESTAMP(), TIMESTAMPADD(hour, 1, CURRENT_TIMESTAMP()), TRUE, FALSE);
