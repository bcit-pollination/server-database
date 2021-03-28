from werkzeug.exceptions import Unauthorized, BadRequest, NotFound

import src.auth.jwt as jwt
import connexion
import src.db.mysql_interface as db
from src.constants_enums.obj_keys import *
from src.constants_enums.privileges import *

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_privilege(uid, org_id, required_privilege):
    if org_id is None:
        raise Unauthorized("No organization associated with uid")
    privilege_tuple = db.get_privilege(org_id, uid)
    if privilege_tuple is None or len(privilege_tuple) == 0:
        raise Unauthorized("You are not authorized")
    privilege = privilege_tuple[0]
    return required_privilege <= privilege


def get_org_id_from_query():
    queries = connexion.request.args
    if queries is None:
        return None
    if OrgInfoKeys.ORG_ID in queries:
        return queries[OrgInfoKeys.ORG_ID]
    return None


def get_election_id_from_query():
    queries = connexion.request.args
    if queries is None:
        return None
    if ElectionKeys.ELECTION_ID in queries:
        return queries[ElectionKeys.ELECTION_ID]
    return None


def check_org_auth(token, body, required_privilege, unauth_msg):
    # sorry world D:
    org_id = None
    if body is None:
        # must be get request
        # attempt to find org_id in query
        org_id = get_org_id_from_query()
        if org_id is None:
            # attempt to find org_id via election
            election_id = get_election_id_from_query()
            if election_id is None:
                # attempt to find org_id via ownership
                org_info = db.get_owner_org_info(token[JwtTokenKeys.UID])
                if org_info is None:
                    raise Unauthorized(unauth_msg)
                else:
                    org_id = org_info[0]
            else:
                election = db.get_election(election_id)
                org_id = election[1]
    elif OrgInfoKeys.ORG_ID not in body:
        if ElectionKeys.ELECTION_ID not in body:
            raise BadRequest("Must include org_id or election_id in the body")
        else:
            election_info = db.get_election(body[ElectionKeys.ELECTION_ID])
            if election_info is None:
                raise NotFound("Election was not found")
            org_id = election_info[1]
    else:
        org_id = body[OrgInfoKeys.ORG_ID]
    if not check_privilege(int(token[JwtTokenKeys.UID]), org_id, required_privilege):
        raise Unauthorized(unauth_msg)


def check_member(token):
    token = check_user(token)
    body = connexion.request.get_json()
    check_org_auth(token, body, PrivilegeLevels.MEMBER, "You must be an organization member to access this endpoint")
    return token


def check_admin(token):
    token = check_user(token)
    body = connexion.request.get_json()
    check_org_auth(token, body, PrivilegeLevels.ADMIN,
                   "You must be an organization administrator to access this endpoint")
    return token


def check_owner(token):
    token = check_user(token)
    body = connexion.request.get_json()
    check_org_auth(token, body, PrivilegeLevels.OWNER, "You must be the organization owner to access this endpoint")
    return token


def check_user(token):
    token_info = jwt.decode_token(token)
    if not db.get_user(token_info[JwtTokenKeys.UID]):
        raise NotFound("User is not found in db")
    return token_info
