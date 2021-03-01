import connexion
import six

from server.swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from server.swagger_server import util
import server.src.db.mysql_interface as db
from server.src.constants_enums.obj_keys import LoginKeys


def login(body):  # noqa: E501
    """Login user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """

    body = connexion.request.get_json()  # noqa: E501
    uid = db.get_uid_with_credentials(body[LoginKeys.EMAIL], body[LoginKeys.PASSWORD])

    return 'do some magic!'
