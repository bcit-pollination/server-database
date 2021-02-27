import connexion
import six

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server import util


def login(unknown_base_type=None):  # noqa: E501
    """Login user

     # noqa: E501

    :param unknown_base_type: 
    :type unknown_base_type: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def logout():  # noqa: E501
    """Login user

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
