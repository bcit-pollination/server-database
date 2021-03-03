from werkzeug.exceptions import Unauthorized, BadRequest, NotFound

import server.src.auth.jwt as jwt
import connexion
import server.src.db.mysql_interface as db
from server.src.constants_enums.obj_keys import *
from server.src.constants_enums.privileges import PrivilegeLevels
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_member(token):
    token = check_user(token)
    body = connexion.request.get_json()
    if OrgInfoKeys.ORG_ID not in body:
        raise BadRequest("Must include org_id in the body")
    if db.get_privilege(token[JwtTokenKeys.UID], body[OrgInfoKeys.ORG_ID]) < PrivilegeLevels.MEMBER:
        raise Unauthorized("You must be an organization member to access this endpoint")
    return token


def check_admin(token):
    token = check_user(token)
    body = connexion.request.get_json()
    if OrgInfoKeys.ORG_ID not in body:
        raise BadRequest("Must include org_id in the body")
    if db.get_privilege(token[JwtTokenKeys.UID], body[OrgInfoKeys.ORG_ID]) < PrivilegeLevels.ADMIN:
        raise Unauthorized("You must be an organization administrator to access this endpoint")
    return token


def check_owner(token):
    token = check_user(token)
    body = connexion.request.get_json()
    if OrgInfoKeys.ORG_ID not in body:
        raise BadRequest("Must include org_id in the body")
    if db.get_privilege(token[JwtTokenKeys.UID], body[OrgInfoKeys.ORG_ID]) < PrivilegeLevels.OWNER:
        raise Unauthorized("You must be the organization owner to access this endpoint")
    return token


def check_user(token):
    token = jwt.decode_token(token)
    if not db.get_user(token[JwtTokenKeys.UID]):
        raise NotFound("User is not found in db")
    return token
