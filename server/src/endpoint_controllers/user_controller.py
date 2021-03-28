from random import random
import secrets
from werkzeug.exceptions import InternalServerError

from src.constants_enums.obj_keys import JwtTokenKeys
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.voting_token import VotingToken  # noqa: E501

import src.db.mysql_interface as db
from src.auth.jwt import generate_token


def create_user(body):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: New user info to be added.
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    user_model = User.from_dict(body)
    fake_voting_token = secrets.token_urlsafe(24)
    uid = db.create_user(user_model, fake_voting_token)
    token = generate_token(uid)
    return InlineResponse200(token)


def get_user(token_info):  # noqa: E501
    """Get user info

     # noqa: E501


    :rtype: User
    """
    user = db.get_user(token_info[JwtTokenKeys.UID])
    return user


def get_voting_token(token_info):  # noqa: E501
    """Get token used to vote

     # noqa: E501


    :rtype: VotingToken
    """
    voting_token = db.get_user_token(token_info[JwtTokenKeys.UID])
    if voting_token is None or len(voting_token) == 0:
        print("Could not find token for: ", token_info)
        raise InternalServerError("Could not retrieve the voting token for one of the voters")
    return VotingToken(voting_token[0])


def remove_user(token_info):  # noqa: E501
    """Remove user from service. Only a user can remove himself, hence the user is infered from the JWT

     # noqa: E501


    :rtype: None
    """
    db.deactivate_user(token_info[JwtTokenKeys.UID])
    return None
