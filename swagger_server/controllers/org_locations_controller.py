import connexion
import six

from swagger_server.models.body3 import Body3  # noqa: E501
from swagger_server.models.body4 import Body4  # noqa: E501
from swagger_server.models.body5 import Body5  # noqa: E501
from swagger_server.models.body6 import Body6  # noqa: E501
from swagger_server.models.inline_response2008 import InlineResponse2008  # noqa: E501
from swagger_server import util


def add_location(body=None):  # noqa: E501
    """Add location

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body5.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_location(body=None):  # noqa: E501
    """Delete location

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body6.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_locations_list(body=None):  # noqa: E501
    """Get all the org voting locations

    In principle this information should be available to the public # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2008
    """
    if connexion.request.is_json:
        body = Body3.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_location(body=None):  # noqa: E501
    """Update location

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body4.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
