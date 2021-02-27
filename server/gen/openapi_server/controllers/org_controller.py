import connexion
import six

from openapi_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from openapi_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from openapi_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.models.verifier_password import VerifierPassword  # noqa: E501
from openapi_server import util


def create_org(unknown_base_type=None):  # noqa: E501
    """Create org

     # noqa: E501

    :param unknown_base_type: Org id is optional
    :type unknown_base_type: dict | bytes

    :rtype: InlineResponse2004
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def disband_org():  # noqa: E501
    """Disband org

    An org can only be disbanded by it&#39;s owner, hence the org is infered from the JWT # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_org(org_id):  # noqa: E501
    """Get org info

     # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: InlineResponse2003
    """
    return 'do some magic!'


def get_org_list():  # noqa: E501
    """Get org info

     # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def get_verifier_password(unknown_base_type=None):  # noqa: E501
    """Get password used by ID verifiers to login into voting machine

     # noqa: E501

    :param unknown_base_type: 
    :type unknown_base_type: dict | bytes

    :rtype: VerifierPassword
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_org(unknown_base_type=None):  # noqa: E501
    """Update org info

     # noqa: E501

    :param unknown_base_type: Org id is optional
    :type unknown_base_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
