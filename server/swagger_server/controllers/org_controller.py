import connexion
import six

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user_org import UserOrg  # noqa: E501
from swagger_server.models.verifier_password import VerifierPassword  # noqa: E501
from swagger_server import util


def create_org(body):  # noqa: E501
    """Create org

     # noqa: E501

    :param body: Org id is optional
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def disband_org():  # noqa: E501
    """Disband org

    An org can only be disbanded by it&#x27;s owner, hence the org is infered from the JWT # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_org(org_id):  # noqa: E501
    """Get org info

     # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: UserOrg
    """
    return 'do some magic!'


def get_org_list():  # noqa: E501
    """Get org info

     # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def get_verifier_password(body):  # noqa: E501
    """Get password used by ID verifiers to login into voting machine

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: VerifierPassword
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_org(body):  # noqa: E501
    """Update org info

     # noqa: E501

    :param body: Org id is optional
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
