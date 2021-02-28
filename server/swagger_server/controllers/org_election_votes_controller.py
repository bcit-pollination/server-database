import connexion
import six

from swagger_server import util


def upload_election_votes(body):  # noqa: E501
    """Create/Update election results

    Create/Update election results. Each call will add a new versioned entry for security purposes.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
