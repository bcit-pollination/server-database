import connexion
import six

from openapi_server.models.election_results import ElectionResults  # noqa: E501
from openapi_server import util


def get_election_results(election_id):  # noqa: E501
    """Get election voting results

    Get the voting results for an election. If the election is private, and the user is not a member of the org, then will respond 401: Unauthorized If there are several results for the same election, the latest version will be  # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: ElectionResults
    """
    return 'do some magic!'
