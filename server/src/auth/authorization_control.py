from werkzeug.exceptions import Unauthorized, BadRequest, NotFound

import src.auth.jwt as jwt
import connexion
import src.db.mysql_interface as db
from src.constants_enums.obj_keys import *
from src.constants_enums.privileges import *
from src.utils.logging import with_exception_log

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


def check_org_auth(token, org_id, required_privilege, unauth_msg):
    if not check_privilege(int(token[JwtTokenKeys.UID]), org_id, required_privilege):
        raise Unauthorized(unauth_msg)


def get_org_id():
    body = connexion.request.get_json()
    if body is None:
        # must be get request
        # attempt to find org_id in query
        org_id = get_org_id_from_query()
        if org_id is None:
            raise Unauthorized("must provide org_id in query")
    elif OrgInfoKeys.ORG_ID not in body:
        raise Unauthorized("You must provide org_id in body")
    else:
        org_id = body[OrgInfoKeys.ORG_ID]
    return org_id


def get_org_id_through_election_id():
    body = connexion.request.get_json()
    if body is None:
        # get request. election id must be in url query
        election_id = get_election_id_from_query()
        if election_id is None:
            raise Unauthorized("Election id must be provided")
    elif ElectionKeys.ELECTION_ID not in body:
        raise Unauthorized("Must include election_id in the body")
    else:
        election_id = body[ElectionKeys.ELECTION_ID]
    election_info = db.get_election(election_id)
    if election_info is None:
        raise NotFound("Election was not found")
    org_id = election_info[1]
    return org_id


def check_member_with_election_id(token):
    print("member")
    token = check_user(token)
    org_id = with_exception_log(get_org_id_through_election_id)()
    with_exception_log(check_org_auth)(token, org_id, PrivilegeLevels.MEMBER, "You must be an organization member to access this endpoint")
    return token


def check_member_with_org_id(token):
    print("member")
    token = check_user(token)
    org_id = with_exception_log(get_org_id)()
    with_exception_log(check_org_auth)(token, org_id, PrivilegeLevels.MEMBER, "You must be an organization member to access this endpoint")
    return token


def check_admin_with_election_id(token):
    print("admin")
    token = check_user(token)
    org_id = with_exception_log(get_org_id_through_election_id)()
    with_exception_log(check_org_auth)(token, org_id, PrivilegeLevels.ADMIN,
                                      "You must be an organization administrator to access this endpoint")
    return token


def check_admin_with_org_id(token):
    print("ADMIN")
    token = check_user(token)
    org_id = with_exception_log(get_org_id)()
    with_exception_log(check_org_auth)(token, org_id, PrivilegeLevels.ADMIN,
                                      f"You must be an organization administrator to access this endpoint")
    return token


def check_owner(token):
    print("owner")
    token = check_user(token)

    org_info = with_exception_log(db.get_owner_org_info)(token[JwtTokenKeys.UID])
    if org_info is None:
        raise Unauthorized("You don't own any org")
    return token


@with_exception_log
def check_user(token):
    print("user")
    token_info = jwt.decode_token(token)
    if not db.get_user(token_info[JwtTokenKeys.UID]):
        raise NotFound("User is not found in db")
    return token_info
