import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.models.location import Location  # noqa: E501
from swagger_server import util


def add_location(body=None):  # noqa: E501
    """Add location

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
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


def update_location(body=None):  # noqa: E501
    """Update location

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Location.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
