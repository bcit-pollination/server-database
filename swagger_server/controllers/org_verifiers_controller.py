import connexion
import six

from swagger_server.models.body8 import Body8  # noqa: E501
from swagger_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from swagger_server import util


def assign_verifier(body=None):  # noqa: E501
    """Assign verifier to location

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_org_verifiers(body=None):  # noqa: E501
    """Get all the verifiers for a given election

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2008
    """
    if connexion.request.is_json:
        body = Body8.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
