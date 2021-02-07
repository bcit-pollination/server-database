import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.org import Org  # noqa: E501
from swagger_server import util


def create_org(body=None):  # noqa: E501
    """Create org

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2003
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def disband_org():  # noqa: E501
    """Disband org

    An org can only be disbanded by it&#x27;s owner, hence the org is infered from the JWT # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_org(body=None):  # noqa: E501
    """Get org info

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_org_list():  # noqa: E501
    """Get org info

     # noqa: E501


    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def update_org(body=None):  # noqa: E501
    """Update org info

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Org.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
