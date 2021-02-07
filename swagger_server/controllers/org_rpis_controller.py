import connexion
import six

from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.body3 import Body3  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server import util


def add_rpi(body):  # noqa: E501
    """Add voting machine

    New RPIs are assigned location 0.   location of 0 can be interpreted as no location assigned  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2006
    """
    if connexion.request.is_json:
        body = Body2.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def assign_rpi(body=None):  # noqa: E501
    """Assign voting machine

     # noqa: E501

    :param body: data needed to associate rpi with a certain location
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def discard_rpi(body=None):  # noqa: E501
    """Discard RPI

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body3.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_rpis(org_id):  # noqa: E501
    """Get the voting machines belonging to this organization

     # noqa: E501

    :param org_id: The id of the org the rpis belong to
    :type org_id: int

    :rtype: InlineResponse2005
    """
    return 'do some magic!'
