import connexion
import six

from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server import util


def upload_election_votes(unknown_base_type=None):  # noqa: E501
    """Create/Update election results

    Create/Update election results. Each call will add a new versioned entry for security purposes.  # noqa: E501

    :param unknown_base_type: 
    :type unknown_base_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
