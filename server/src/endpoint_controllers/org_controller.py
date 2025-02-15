import base64

from werkzeug.exceptions import NotFound

from src.auth.password_hashing import get_hash
from swagger_server.models import Org
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user_org import UserOrg  # noqa: E501
from swagger_server.models.verifier_password import VerifierPassword  # noqa: E501
import src.db.mysql_interface as db
from src.constants_enums.obj_keys import *


def create_org(body, token_info):  # noqa
    """Create org

     # noqa: E501

    :param body: Org id is optional
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    name = body[OrgInfoKeys.NAME]
    user_org_id = body[OrgInfoKeys.USER_ORG_ID]
    verifier_password = body[OrgInfoKeys.VERIFIER_PASSWORD]
    verifier_password_hash = get_hash(verifier_password)
    org_id = db.create_org(token_info[JwtTokenKeys.UID], name, verifier_password_hash, user_org_id)
    return org_id


def disband_org(token_info):  # noqa: E501
    """Disband org

    An org can only be disbanded by it&#x27;s owner, hence the org is infered from the JWT # noqa: E501


    :rtype: None
    """
    uid = token_info[UserInfoKeys.UID]
    db.disband_org(uid)
    return None


def db_org_to_UserOrg(org_id, name, user_org_id, privilege):
    return UserOrg(org_id, name, privilege, user_org_id)


def get_org(org_id, token_info):  # noqa
    """Get org info

     # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: UserOrg
    """
    org = db.get_organization(org_id, token_info[UserInfoKeys.UID])
    if org is None:
        raise NotFound("No such org")
    user_org = db_org_to_UserOrg(org_id, org[1], org[3], org[2])
    return user_org


def get_org_list(token_info):  # noqa: E501
    """Get org info

     # noqa: E501


    :rtype: InlineResponse2001
    """
    uid = token_info[UserInfoKeys.UID]
    org_list = db.get_user_org_list(uid)
    user_org_list = []
    for org in org_list:
        user_org_list.append(db_org_to_UserOrg(org[0], org[1], org[3], org[2]))
    org_list_model = InlineResponse2001(user_org_list)
    return org_list_model


def get_verifier_password(body):  # noqa: E501
    """Get password used by ID verifiers to login into voting machine

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: VerifierPassword
    """
    org_id = body[OrgInfoKeys.ORG_ID]
    verifier_password = db.get_verifier_password(org_id)[0]
    encoded_verifier_password = base64.b64encode(verifier_password).decode('utf-8')
    return VerifierPassword(encoded_verifier_password)


def update_org(body, token_info):  # noqa
    """Update org info

     # noqa: E501

    :param body: Org id is optional
    :type body: dict | bytes

    :rtype: None
    """
    name = body[OrgInfoKeys.NAME]
    verifier_password = body[OrgInfoKeys.VERIFIER_PASSWORD]
    org_id_tuple = db.get_owner_org_info(token_info[JwtTokenKeys.UID])
    org_id = org_id_tuple[0]
    db.update_organization(org_id, name, verifier_password)
    return None
