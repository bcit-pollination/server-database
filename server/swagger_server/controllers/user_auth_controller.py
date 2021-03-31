import connexion
import six

from src.utils.logging import with_exception_log
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from src.endpoint_controllers import user_auth_controller as ctl


@with_exception_log
def login(body):  # noqa: E501
    """Login user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    return ctl.login(body)
