import MySQLdb

from server.swagger_server.models.user import User
from server.src.constants_enums.privileges import PrivilegeLevels
from .procedures import PROCEDURE


def get_db_connection() -> MySQLdb.Connection:
    return MySQLdb.connect(read_default_file='~/.my.cnf')


def call_proc(proc_name, args=None, resp_many=False):
    resp = None

    try:
        with get_db_connection() as db:
            with db.cursor() as cursor:
                print("Calling proc:", proc_name, args)
                cursor.callproc(proc_name, args)
                if resp_many:
                    resp = cursor.fetchall()
                else:
                    resp = cursor.fetchone()
                print("Database return:", resp)
            db.commit()
    except MySQLdb.MySQLError as err:
        print("SQL process failed:", err)
    finally:
        return resp


def get_uid_with_credentials(email, password):
    return call_proc(PROCEDURE.LOGINUSER, (email, password))


def create_user(user: User) -> int:
    user = call_proc(PROCEDURE.CREATEUSER, (user.first_name,
                                            user.last_name,
                                            user.email,
                                            "2021-02-15",
                                            user.password,
                                            "test_token"))
    return user[0] if user else user


def add_user_to_org(user_id, user_org_id, email):
    return call_proc(PROCEDURE.ENROLLUSER, (user_id, user_org_id, email))


def get_user(uid):
    user = call_proc(PROCEDURE.GETUSER, (uid,))
    if user:
        print(user)
        user = User.from_dict(dict(id=user[0], first_name=user[1], last_name=user[2], email=user[3], dob=user[4]))
    return user


def create_org(org_name, user_org_id, user_id, verifier_password):
    return call_proc(PROCEDURE.CREATEORG, (user_id, org_name, user_org_id, verifier_password))


def get_users_organization(user_id):
    return call_proc(PROCEDURE.GETUSERORGANIZATION, (user_id,))


def get_user_elections(user_id):
    return call_proc(PROCEDURE.GETUSERELECTIONS, (user_id,), resp_many=True)


def get_organization_users(org_id):
    return call_proc(PROCEDURE.GETORGANIZATIONUSERS, (org_id,), resp_many=True)


def get_user_elections_alternate(user_id):
    return call_proc(PROCEDURE.GETUSERELECTIONSALTERNATE, (user_id,), resp_many=True)


def update_user(user_id, first_name, last_name, email, password):
    return call_proc(PROCEDURE.UPDATEUSER, (user_id, first_name, last_name, email, password))


def deactivate_user(user_id):
    return call_proc(PROCEDURE.DEACTIVATEUSER, (user_id,))


def get_user_token(user_id):
    return call_proc(PROCEDURE.GETUSERTOKEN, (user_id,))


def get_organizations(user_id):
    return call_proc(PROCEDURE.GETORGANIZATIONS, (user_id,), resp_many=True)


def get_organization(org_id):
    return call_proc(PROCEDURE.GETORGANIZATION, (org_id,))


def update_organization(org_id, org_name, verifier_password):
    return call_proc(PROCEDURE.UPDATEORGANIZATION, (org_id, org_name,verifier_password))


def disband_org(uid):
    return call_proc(PROCEDURE.DISBANDORG, (uid,))


def get_verifier_password(org_id):
    return call_proc(PROCEDURE.GETVERIFIERPASSWORD, (org_id,))


def get_users_from_org(org_id):
    return call_proc(PROCEDURE.GETUSERSFROMORG, (org_id,), resp_many=True)


def update_privilege(user_id, org_id, privilege_level: PrivilegeLevels):
    return call_proc(PROCEDURE.UPDATEPRIVILEGE, (user_id, org_id, privilege_level))


def invite_user(user_id, org_id, user_org_id):
    return call_proc(PROCEDURE.INVITEUSER, (user_id, org_id, user_org_id))


def create_election(org_id, description, start_time, end_time, is_public, anonymous):
    return call_proc(PROCEDURE.CREATEELECTION, (org_id, description, start_time, end_time, is_public, anonymous))


def update_election(election_id, description, start_time, end_time, is_public, anonymous):
    return call_proc(PROCEDURE.UPDATEELECTION, (election_id, description, start_time, end_time, is_public, anonymous))


def delete_election(election_id):
    return call_proc(PROCEDURE.DELETEELECTION, (election_id,))


def get_election(election_id):
    return call_proc(PROCEDURE.GETELECTION, (election_id,))


def get_org_elections(org_id):
    return call_proc(PROCEDURE.GETELECTIONLISTORG, (org_id,), resp_many=True)


def get_election_votes(election_id):
    return call_proc(PROCEDURE.GETINDIVIDUALVOTES, (election_id,), resp_many=True)


def get_question_opt(question_id):
    return call_proc(PROCEDURE.GETQUESTIONOPT, (question_id,))


def get_election_questions(election_id):
    return call_proc(PROCEDURE.GETELECTIONQUESTIONS, (election_id,))


def get_public_elections():
    return call_proc(PROCEDURE.GETPUBLICELECTIONS, (None,), resp_many=True)


def add_questions(election_id, description):
    return call_proc(PROCEDURE.ADDQUESTION, (election_id, description), resp_many=True)


def drop_question(question_id):
    return call_proc(PROCEDURE.ADDQUESTION, (question_id,))


def update_question(question_id, description):
    return call_proc(PROCEDURE.UPDATEQUESTION, (question_id, description))


def add_question_opt(opt_id):
    return call_proc(PROCEDURE.ADDOPT, (opt_id,))


def remove_question_opt(opt_id):
    return call_proc(PROCEDURE.DROPOPT, (opt_id,))


def update_question_opt(opt_id, description):
    return call_proc(PROCEDURE.DROPOPT, (opt_id, description))


def get_privilege(org_id, user_id):
    return call_proc(PROCEDURE.GETPRIVILEGE, (org_id, user_id))


def get_idvt(election_id):
    return call_proc(PROCEDURE.GETPRIVILEGE, (election_id,))


def create_vote(voting_token, time_stamp):
    return call_proc(PROCEDURE.CREATEVOTE, (voting_token, time_stamp))


def create_choice(vote_id, opt_id):
    return call_proc(PROCEDURE.CREATEVOTE, (vote_id, opt_id))
