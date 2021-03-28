import connexion
import six

from src.utils.election_parsing import parse_election_tuples
from swagger_server import util
import src.db.mysql_interface as db
from swagger_server.models.inline_response2009 import InlineResponse2009


def get_public_election_result_list(page, elections_per_page):  # noqa: E501
    """Get public elections

    Get a list of elections with results open to the public  # noqa: E501

    :param page: The page to get
    :type page: int
    :param elections_per_page: The page to get
    :type elections_per_page: int

    :rtype: InlineResponse2009
    """
    election_tuples = db.get_public_elections(elections_per_page, page)
    elections = parse_election_tuples(election_tuples)
    return InlineResponse2009(elections)

