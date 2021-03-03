import connexion
import six
from werkzeug.exceptions import NotFound

from server.swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from server.swagger_server.models.user import User  # noqa: E501
from server.swagger_server.models.voting_token import VotingToken  # noqa: E501
from server.swagger_server import util

import server.src.db.mysql_interface as db
from server.src.auth.jwt import generate_token
from server.src.constants_enums.obj_keys import *


def app_create_user(body):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: New user info to be added.
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    userModel = User.from_dict(body)
    uid = db.create_user(userModel)
    token = generate_token(uid)
    return InlineResponse200(token)


def get_user(token_info):  # noqa: E501
    """Get user info

     # noqa: E501


    :rtype: User
    """
    user = db.get_user(token_info[JwtTokenKeys.UID])
    return User.from_dict(user)


def get_voting_token(token_info):  # noqa: E501
    """Get token used to vote

     # noqa: E501


    :rtype: VotingToken
    """
    voting_token = db.get_user_token(token_info[JwtTokenKeys.UID])
    return VotingToken(voting_token)


def remove_user(token_info):  # noqa: E501
    """Remove user from service. Only a user can remove himself, hence the user is infered from the JWT

     # noqa: E501


    :rtype: None
    """
    db.deactivate_user(token_info[JwtTokenKeys.UID])
    return None
