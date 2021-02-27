import connexion
import six

from openapi_server.models.election import Election  # noqa: E501
from openapi_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from openapi_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from openapi_server.models.inline_response2009 import InlineResponse2009  # noqa: E501
from openapi_server import util


def create_election(election=None):  # noqa: E501
    """Create election

    Create election # noqa: E501

    :param election: Election ID is not required to POST
    :type election: dict | bytes

    :rtype: InlineResponse2009
    """
    if connexion.request.is_json:
        election = Election.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_election(election_id):  # noqa: E501
    """Delete election

    Elections can only be deleted before they have commenced.  # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_election(election_id):  # noqa: E501
    """Get election info

    Get one election # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: InlineResponse2008
    """
    return 'do some magic!'


def get_election_list(org_id):  # noqa: E501
    """Get election info list

    Get list of elections for a given org # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: InlineResponse2007
    """
    return 'do some magic!'


def update_election(election=None):  # noqa: E501
    """update election

    Update election. Elections can only be updated before they have commenced.  # noqa: E501

    :param election: Election ID is not required to POST
    :type election: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        election = Election.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
