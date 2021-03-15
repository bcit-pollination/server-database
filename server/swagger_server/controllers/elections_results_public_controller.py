import connexion
import six

from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server import util
import src.endpoint_controllers.elections_results_public_controller as ctl


def get_public_election_result_list(page, elections_per_page):  # noqa: E501
    """Get public elections

    Get a list of elections with results open to the public  # noqa: E501

    :param page: The page to get
    :type page: int
    :param elections_per_page: The page to get
    :type elections_per_page: int

    :rtype: InlineResponse2006
    """
    return ctl.get_public_election_result_list(page, elections_per_page)
