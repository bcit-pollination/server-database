use voting_system;

insert into Users (user_id, first_name, last_name, email, dob, password, voting_token, deactivated)
values (40, "test_name", "test_last", "test_email", "1990-03-03", "badpass", "votok1", 0),
       (41, "test_name", "test_last", "test_email1", "1990-03-03", "badpass", "votok2", 0),
       (42, "test_name", "test_last", "test_email2", "1990-03-03", "badpass", "votok3", 0),
       (43, "test_name", "test_last", "test_email3", "1990-03-03", "badpass", "votok4", 0),
       (44, "test_name", "test_last", "test_email4", "1990-03-03", "badpass", "votok5", 0),
       (45, "test_name", "test_last", "test_email5", "1990-03-03", "badpass", "votok6", 0),
       (46, "test_name", "test_last", "test_email6", "1990-03-03", "badpass", "votok7", 0),
       (47, "test_name", "test_last", "test_email7", "1990-03-03", "badpass", "votok8", 0),
       (48, "test_name", "test_last", "test_email8", "1990-03-03", "badpass", "votok9", 0),
       (49, "test_name", "test_last", "test_email9", "1990-03-03", "badpass", "votok10", 0);

insert into Organization (org_id, org_name, verifier_password, disabled)
values (10, "test_org", "test_veripass", 0);

insert into Enrollment (enrollment_id, user_id, org_id, privilege, user_org_id)
values (10, 40, 10, 4, "test_user_org_id"),
       (11, 41, 10, 2, "test_user_org_id"),
       (12, 42, 10, 2, "test_user_org_id"),
       (13, 43, 10, 2, "test_user_org_id"),
       (14, 44, 10, 2, "test_user_org_id"),
       (15, 45, 10, 2, "test_user_org_id"),
       (16, 46, 10, 2, "test_user_org_id"),
       (17, 47, 10, 2, "test_user_org_id"),
       (18, 48, 10, 1, "test_user_org_id");

insert into Election (election_id, org_id, election_description, start_time, end_time, anonymous, public_results,
                      verified)
values (10, 10, "test_elec", "2000-01-23T04:56:07+00:00", "2024-01-23T04:56:07+00:00", 1, 1, 1);

insert into Question (question_id, election_id, question_description, min_selection_count, max_selection_count,
                      priority_selections)
values (10, 10, "q1", 2, 2, 0),
       (11, 10, "q2", 1, 1, 0),
       (12, 10, "q3", 3, 3, 1);

insert into Opt (option_id, question_id, option_description, total_votes_for)
values (20, 10, "q1_op1", 0),
       (21, 10, "q1_op2", 0),
       (22, 10, "q1_op3", 0),
       (23, 11, "q2_op1", 0),
       (24, 11, "q2_op2", 0),
       (25, 12, "q3_op1", 0),
       (26, 12, "q3_op2", 0),
       (27, 12, "q3_op3", 0);