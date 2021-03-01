import connexion
import six
from werkzeug.exceptions import Unauthorized

from server.swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from server.swagger_server import util
import server.src.db.mysql_interface as db
from server.src.constants_enums.obj_keys import LoginKeys
from server.src.auth.jwt import generate_token


def login(body):  # noqa: E501
    """Login user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """

    uid = db.get_uid_with_credentials(body[LoginKeys.EMAIL], body[LoginKeys.PASSWORD])
    if uid is None:
        raise Unauthorized("Incorrect credentials")
    return generate_token(uid)
