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
    name = body[OrgInfoKeys.ORG_INFO][OrgInfoKeys.NAME]
    user_org_id = body[OrgInfoKeys.USER_ORG_ID]
    verifier_password = body[OrgInfoKeys.VERIFIER_PASSWORD]
    org_id = db.create_org(token_info[JwtTokenKeys.UID], name, verifier_password, user_org_id)
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
    return UserOrg(privilege, user_org_id, Org(org_id, name))



def get_org(org_id):  # noqa: E501
    """Get org info

     # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: UserOrg
    """
    org = db.get_organization(org_id)
    # TODO
    return db_org_to_UserOrg(org_id, "fake_name", "fake id", -2)


def get_org_list(token_info):  # noqa: E501
    """Get org info

     # noqa: E501


    :rtype: InlineResponse2001
    """
    uid = token_info[UserInfoKeys.UID]
    org_list = db.get_user_org_list(uid)
    return org_list


def get_verifier_password(body):  # noqa: E501
    """Get password used by ID verifiers to login into voting machine

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: VerifierPassword
    """
    org_id = body[OrgInfoKeys.ORG_ID]
    verifier_password = db.get_verifier_password(org_id)
    return verifier_password


def update_org(body):  # noqa: E501
    """Update org info

     # noqa: E501

    :param body: Org id is optional
    :type body: dict | bytes

    :rtype: None
    """
    name = body[OrgInfoKeys.ORG_INFO][OrgInfoKeys.NAME]
    verifier_password = body[OrgInfoKeys.VERIFIER_PASSWORD]
    org_id = body[OrgInfoKeys.ORG_ID]
    db.update_organization(org_id, name, verifier_password)
    return None
