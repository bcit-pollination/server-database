import connexion
import six

from src.utils.logging import with_exception_log
from swagger_server import util
import src.endpoint_controllers.org_election_votes_controller as ctl


@with_exception_log
def upload_election_votes(body):  # noqa: E501
    """Create/Update election results

    Create/Update election results. Each call will add a new versioned entry for security purposes.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    return ctl.upload_election_votes(body)
