import connexion
import six

from src.utils.logging import with_exception_log
from swagger_server.models.election_results import ElectionResults  # noqa: E501
from swagger_server import util
import src.endpoint_controllers.org_election_results_controller as ctl


@with_exception_log
def get_election_results(election_id, token_info):  # noqa: E501
    """Get election voting results

    Get the voting results for an election. If the election is private, and the user is not a member of the org, then will respond 401: Unauthorized Note that the options in questions may take the shape of Option or option_results  # noqa: E501

    :rtype: ElectionResults
    """
    return ctl.get_election_results(election_id, token_info)
