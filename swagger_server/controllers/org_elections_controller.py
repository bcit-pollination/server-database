import connexion
import six

from swagger_server.models.body7 import Body7  # noqa: E501
from swagger_server.models.body8 import Body8  # noqa: E501
from swagger_server.models.body9 import Body9  # noqa: E501
from swagger_server.models.election import Election  # noqa: E501
from swagger_server.models.inline_response20010 import InlineResponse20010  # noqa: E501
from swagger_server.models.inline_response20011 import InlineResponse20011  # noqa: E501
from swagger_server.models.inline_response2009 import InlineResponse2009  # noqa: E501
from swagger_server import util


def create_election(body=None):  # noqa: E501
    """Create election

    Create election # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20011
    """
    if connexion.request.is_json:
        body = Election.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_election(body=None):  # noqa: E501
    """Delete election

    Elections can only be deleted before they have commenced.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body9.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_election(body=None):  # noqa: E501
    """Get election info

    Get one election # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20010
    """
    if connexion.request.is_json:
        body = Body8.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_election_list(body=None):  # noqa: E501
    """Get election info list

    Get list of elections for a given org # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2009
    """
    if connexion.request.is_json:
        body = Body7.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_election(body=None):  # noqa: E501
    """update election

    Update election.  Elections can only be updated before they have commenced.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Election.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
