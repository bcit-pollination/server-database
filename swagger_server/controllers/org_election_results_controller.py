import connexion
import six

from swagger_server.models.election_results import ElectionResults  # noqa: E501
from swagger_server import util


def get_election_results(body=None):  # noqa: E501
    """Get election voting results

    Get the voting results for an election. If the election is private, and the user is not a member  of the org, then will respond 401: Unauthorized If there are several results for the same election, the latest version will be   # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ElectionResults
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
