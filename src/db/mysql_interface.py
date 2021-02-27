import MySQLdb

from contextlib import closing
from swagger_server.models.user import User
from swagger_server.models.org import Org


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


class PROCEDURE:
    # name                    = proc_name                   # procedure parameters
    LOGINUSER                 = 'LoginUser'                 # email, password
    CREATEUSER                = 'CreateUser'                # first_name, last_name, email, dob, password, voting_token
    CREATEORG                 = 'CreateOrg'                 # user_id, org_name
    ENROLLUSER                = 'EnrollUser'                # user_id, org_id
    GETUSER                   = 'GetUser'                   # user_id
    GETUSERORGANIZATION       = 'GetUserOrganization'       # user_id
    GETUSERELECTIONS          = 'GetUserElections'          # user_id
    GETORGANIZATIONUSERS      = 'GetOrganizationUsers'      # org_id
    GETUSERELECTIONSALTERNATE = 'GeUserElectionsAlternate'  # user_id
