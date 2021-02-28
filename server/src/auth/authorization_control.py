import six
from werkzeug.exceptions import Unauthorized, BadRequest

import server.src.auth.jwt as jwt
import connexion
import server.src.db.mysql_interface as db
import server.src.obj_keys as obj_keys
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""

MEMBER_PRIV = 1
ADMIN_PRIV = 2
OWNER_PRIV = 3


def check_member(token):
    token = check_user(token)
    body = connexion.request.get_json()
    if obj_keys.ORG_ID not in body:
        raise BadRequest("Must include org_id in the body")
    if db.get_privilege(token[jwt.JWT_UID_KEY], body[obj_keys.ORG_ID]) < MEMBER_PRIV:
        raise Unauthorized("You must be an organization member to access this endpoint")
    return token


def check_admin(token):
    token = check_user(token)
    body = connexion.request.get_json()
    if obj_keys.ORG_ID not in body:
        raise BadRequest("Must include org_id in the body")
    if db.get_privilege(token[jwt.JWT_UID_KEY], body[obj_keys.ORG_ID]) < ADMIN_PRIV:
        raise Unauthorized("You must be an organization administrator to access this endpoint")
    return token


def check_owner(token):
    token = check_user(token)
    body = connexion.request.get_json()
    if obj_keys.ORG_ID not in body:
        raise BadRequest("Must include org_id in the body")
    if db.get_privilege(token[jwt.JWT_UID_KEY], body[obj_keys.ORG_ID]) < OWNER_PRIV:
        raise Unauthorized("You must be the organization owner to access this endpoint")
    return token


def check_user(token):
    token = jwt.decode_token(token)
    if not db.get_user(token[jwt.JWT_UID_KEY]):
        raise Unauthorized("User is not found in db")
    return token
