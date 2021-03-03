import connexion
import six

from swagger_server.models.election_results import ElectionResults  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server import util


def get_public_election_result(election_id):  # noqa: E501
    """Get public elections

    Get a list of elections with results open to the public  # noqa: E501

    :param election_id: The id of the election to get
    :type election_id: int

    :rtype: ElectionResults
    """
    return 'do some magic!'


def get_public_election_result_list(page, elections_per_page):  # noqa: E501
    """Get public elections

    Get a list of elections with results open to the public  # noqa: E501

    :param page: The page to get
    :type page: int
    :param elections_per_page: The page to get
    :type elections_per_page: int

    :rtype: InlineResponse2006
    """
    return 'do some magic!'
