import MySQLdb

from contextlib import closing
from swagger_server.models.user import User
from swagger_server.models.org import Org
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


def update_user(user: User):
    return call_proc(PROCEDURE.UPDATEUSER, (user.id, user.first_name, user.last_name, user.email, user.password))


def deactivate_user(user: User):
    return call_proc(PROCEDURE.DEACTIVATEUSER, (user.id,))


def get_user_token(user: User):
    return call_proc(PROCEDURE.GETUSERTOKEN, (user.id,))


def get_organizations(user: User):
    return call_proc(PROCEDURE.GETORGANIZATIONS, (user.id,), resp_many=True)


def get_arganization(org: Org):
    return call_proc(PROCEDURE.GETORGANIZATION, (org.id,))


def get_user_elections_alternate(user: User):
    return call_proc(PROCEDURE.GETUSERELECTIONSALTERNATE, (user.id,), resp_many=True)


def get_user_elections_alternate(user: User):
    return call_proc(PROCEDURE.GETUSERELECTIONSALTERNATE, (user.id,), resp_many=True)


def get_user_elections_alternate(user: User):
    return call_proc(PROCEDURE.GETUSERELECTIONSALTERNATE, (user.id,), resp_many=True)


def get_user_elections_alternate(user: User):
    return call_proc(PROCEDURE.GETUSERELECTIONSALTERNATE, (user.id,), resp_many=True)


def get_user_elections_alternate(user: User):
    return call_proc(PROCEDURE.GETUSERELECTIONSALTERNATE, (user.id,), resp_many=True)
