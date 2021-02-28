import MySQLdb

from swagger_server.models.user import User
from .privileges import PRIVILEGE
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


def add_user_to_org(user_id, org_id):
    return call_proc(PROCEDURE.ENROLLUSER, (user_id, org_id))


def get_user(uid):
    user = call_proc(PROCEDURE.GETUSER, (uid,))
    if user:
        print(user)
        user = User.from_dict(dict(id=user[0], first_name=user[1], last_name=user[2], email=user[3], dob=user[4]))
    return user


def create_org(org_name, user_id):
    return call_proc(PROCEDURE.CREATEORG, (user_id, org_name, "temp holder"))


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


def update_organization(org_id, org_name):
    return call_proc(PROCEDURE.UPDATEORGANIZATION, (org_id, org_name))


def disband_org(org_id):
    return call_proc(PROCEDURE.DISBANDORG, (org_id,))


def get_verifier_password(user_id):
    return call_proc(PROCEDURE.GETVERIFIERPASSWORD, (user_id,))


def get_users_from_org(org_id):
    return call_proc(PROCEDURE.GETUSERSFROMORG, (org_id,), resp_many=True)


def update_privilege(user_id, privilege_level: PRIVILEGE):
    return call_proc(PROCEDURE.UPDATEPRIVILEGE, (user_id, privilege_level))


def invite_user(user_id, org_id):
    return call_proc(PROCEDURE.INVITEUSER, (user_id, org_id))


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

