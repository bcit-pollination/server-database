import connexion
import six

from swagger_server.models.election_results import ElectionResults  # noqa: E501
from swagger_server.models.inline_response20012 import InlineResponse20012  # noqa: E501
from swagger_server import util


def get_public_election_result(election_id, version=None):  # noqa: E501
    """Get public elections

    Get a list of elections with results open to the public  # noqa: E501

    :param election_id: The id of the election to get
    :type election_id: int
    :param version: Optional, the voting result version. Leave empty for latest
    :type version: int

    :rtype: ElectionResults
    """
    return 'do some magic!'


def get_public_election_result_list(page, elections_per_page, version=None):  # noqa: E501
    """Get public elections

    Get a list of elections with results open to the public  # noqa: E501

    :param page: The page to get
    :type page: int
    :param elections_per_page: The page to get
    :type elections_per_page: int
    :param version: Optional, the voting result version. Leave empty for latest
    :type version: int

    :rtype: InlineResponse20012
    """
    return 'do some magic!'
