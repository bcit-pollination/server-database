from werkzeug.exceptions import Unauthorized

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
import src.db.mysql_interface as db
from src.constants_enums.obj_keys import LoginKeys
from src.auth.jwt import generate_token
from src.auth.password_hashing import check_password


def login(body):  # noqa: E501
    """Login user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    password_hash_tuple = db.get_user_id(body[LoginKeys.EMAIL])
    if password_hash_tuple is None or len(password_hash_tuple) == 0:
        raise Unauthorized("Incorrect credentials")
    uid = password_hash_tuple[0]
    password_hash = password_hash_tuple[1]
    if not check_password(body[LoginKeys.PASSWORD], password_hash):
        raise Unauthorized("Incorrect credentials")
    return InlineResponse200(generate_token(uid))
