import connexion
import six

from swagger_server.models.inline_response20013 import InlineResponse20013  # noqa: E501
from swagger_server import util


def download_voting_package(body=None):  # noqa: E501
    """Download main RPI election package

    Gives the necessary information for a completely standalone voting process. The information included is:   - Complete voter list, including their respective identification within the org and voting token   - Ballot, including the election details and questions   - List of locations   - List of voting machines, each associated to a location   - OPTIONAL. Approved verifier list, each associated to a location.     This property will only be present if the election is verified  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20013
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
