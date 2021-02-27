import connexion
import six

from openapi_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from openapi_server.models.location import Location  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server import util


def add_location(unknown_base_type=None):  # noqa: E501
    """Add location

     # noqa: E501

    :param unknown_base_type: 
    :type unknown_base_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_location(election_id):  # noqa: E501
    """Delete location

     # noqa: E501

    :param election_id: The id of the location
    :type election_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_locations_list(election_id):  # noqa: E501
    """Get all the org voting locations

    In principle this information should be available to the public # noqa: E501

    :param election_id: The id of the location
    :type election_id: int

    :rtype: InlineResponse2006
    """
    return 'do some magic!'


def update_location(location=None):  # noqa: E501
    """Update location

     # noqa: E501

    :param location: 
    :type location: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        location = Location.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
