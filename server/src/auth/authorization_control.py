import six
from werkzeug.exceptions import Unauthorized

import jwt
import connexion
import server.src.db.mysql_interface as db

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_admin(token):
    return {'test_key': 'test_value'}

def check_member(token):
    return {'test_key': 'test_value'}

def check_owner(token):
    token = jwt.decode_token(token)
    if not db.get_user(token[jwt.JWT_UID_KEY]):
        raise Unauthorized("User is not found in db")
    body = connexion.request.get_json()

    privilege =
    return {'test_key': 'test_value'}


def check_user(token):
    token = jwt.decode_token(token)
    if not db.get_user(token[jwt.JWT_UID_KEY]):
        raise Unauthorized("User is not found in db")
    return token
