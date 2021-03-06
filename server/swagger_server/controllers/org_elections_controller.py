import connexion
import six

from swagger_server.models.election import Election  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server import util
from src.endpoint_controllers import org_elections_controller


def create_election(body):  # noqa: E501
    """Create election

    Create election # noqa: E501

    :param body: Election ID is not required to POST
    :type body: dict | bytes

    :rtype: InlineResponse2005
    """
    return org_elections_controller.create_election(body)


def delete_election(election_id):  # noqa: E501
    """Delete election

    Elections can only be deleted before they have commenced.  # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: None
    """
    return org_elections_controller.delete_election(election_id)


def get_election(election_id):  # noqa: E501
    """Get election info

    Get one election # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: Election
    """
    return org_elections_controller.get_election(election_id)


def get_election_list(org_id):  # noqa: E501
    """Get election info list

    Get list of elections for a given org # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: InlineResponse2004
    """
    return 'do some magic!'


def update_election(body):  # noqa: E501
    """update election

    Update election. Elections can only be updated before they have commenced.  # noqa: E501

    :param body: Election ID is not required to POST
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Election.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
