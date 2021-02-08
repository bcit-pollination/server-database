import MySQLdb
from swagger_server.models.user import User


def get_db_connection() -> MySQLdb.Connection:
    return MySQLdb.connect(read_default_file='~/.my.cnf')


def get_uid_with_credentials(email, password):
    with get_db_connection() as db:
        c = db.cursor()
        c.execute("")
        return c.fetchone()


def create_user(user: User):
    with get_db_connection() as db:
        c = db.cursor()
        c.execute("""CALL CreateUser(
        %(first_name),
        %(last_name),
        %(email),
        %(DOB),
        %(password_salt),
        %(password_hash),
        %(voting_token))""",
                  (user.first_name,
                   user.last_name,
                   user.email,
                   user.dob,
                   user.password,
                   "foo",
                   "vote with this!"))
        result = c.fetchone()
        print(result)
        return result


def get_user(uid):
    with get_db_connection() as db:
        c = db.cursor()
        c.execute("")
        return c.fetchone()
