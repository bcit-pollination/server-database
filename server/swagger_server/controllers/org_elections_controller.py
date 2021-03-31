import connexion
import six

from src.utils.logging import with_exception_log
from swagger_server.models.election import Election  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server import util
from src.endpoint_controllers import org_elections_controller as ctl


@with_exception_log
def create_election(body):  # noqa: E501
    """Create election

    Create election # noqa: E501

    :param body: Election ID is not required to POST
    :type body: dict | bytes

    :rtype: InlineResponse2005
    """
    return ctl.create_election(body)


@with_exception_log
def delete_election(election_id):  # noqa: E501
    """Delete election

    Elections can only be deleted before they have commenced.  # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: None
    """
    return ctl.delete_election(election_id)


@with_exception_log
def get_election(election_id):  # noqa: E501
    """Get election info

    Get one election # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: Election
    """
    return ctl.get_election(election_id)


@with_exception_log
def get_election_list(org_id):  # noqa: E501
    """Get election info list

    Get list of elections for a given org # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: InlineResponse2004
    """
    return ctl.get_election_list(org_id)


@with_exception_log
def update_election(body):  # noqa: E501
    """update election

    Update election. Elections can only be updated before they have commenced.  # noqa: E501

    :param body: Election ID is not required to POST
    :type body: dict | bytes

    :rtype: None
    """

    return ctl.update_election(body)
