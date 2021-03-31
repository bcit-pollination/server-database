import connexion
import six

from src.utils.logging import with_exception_log
from swagger_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from swagger_server import util
from src.endpoint_controllers import org_election_download_controller as ctl


@with_exception_log
def download_voting_package(election_id):  # noqa: E501
    """Download main RPI election package

    Gives the necessary information for a completely standalone voting process. The information included is:   - Complete voter list, including their respective identification within the org and voting token   - Ballot, including the election details and questions   - List of locations   - Verifier password  # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: InlineResponse2007
    """
    return ctl.download_voting_package(election_id)
