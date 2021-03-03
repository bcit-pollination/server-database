import connexion
import six

from server.swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from server.swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from server.swagger_server.models.user_org import UserOrg  # noqa: E501
from server.swagger_server.models.verifier_password import VerifierPassword  # noqa: E501
from server.swagger_server import util
import server.src.db.mysql_interface as db
from server.src.constants_enums.obj_keys import *


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
    # TODO create_org
    return 'do some magic!'


def disband_org(token_info):  # noqa: E501
    """Disband org

    An org can only be disbanded by it&#x27;s owner, hence the org is infered from the JWT # noqa: E501


    :rtype: None
    """
    uid = token_info[UserInfoKeys.UID]
    db.disband_org(uid)
    return None


def get_org(org_id):  # noqa: E501
    """Get org info

     # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: UserOrg
    """
    org = db.get_organization(org_id)
    return org


def get_org_list(token_info):  # noqa: E501
    """Get org info

     # noqa: E501


    :rtype: InlineResponse2001
    """
    uid = token_info[UserInfoKeys.UID]
    org_list = db.get_organizations(uid)
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
    # TODO update org
    db.update_organization()
    return None
