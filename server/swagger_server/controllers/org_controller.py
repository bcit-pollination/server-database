import connexion
import six

from src.utils.logging import with_exception_log
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user_org import UserOrg  # noqa: E501
from swagger_server.models.verifier_password import VerifierPassword  # noqa: E501
from swagger_server import util
from src.endpoint_controllers import org_controller as ctl


@with_exception_log
def create_org(body, token_info):  # noqa
    """Create org

     # noqa: E501

    :param body: Org id is optional
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    return ctl.create_org(body, token_info)


@with_exception_log
def disband_org(token_info):  # noqa: E501
    """Disband org

    An org can only be disbanded by it&#x27;s owner, hence the org is inferred from the JWT # noqa: E501


    :rtype: None
    """
    return ctl.disband_org(token_info)


@with_exception_log
def get_org(org_id):  # noqa: E501
    """Get org info

     # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: UserOrg
    """
    return ctl.get_org(org_id)


@with_exception_log
def get_org_list(token_info):  # noqa: E501
    """Get org info

     # noqa: E501


    :rtype: InlineResponse2001
    """
    return ctl.get_org_list(token_info)


@with_exception_log
def get_verifier_password(body):  # noqa: E501
    """Get password used by ID verifiers to login into voting machine

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: VerifierPassword
    """
    return ctl.get_verifier_password(body)


@with_exception_log
def update_org(body):  # noqa: E501
    """Update org info

     # noqa: E501

    :param body: Org id is optional
    :type body: dict | bytes

    :rtype: None
    """
    return ctl.update_org(body)
