import connexion
import six
import src.db.mysql_interface as db

from swagger_server.models import User
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.voting_token import VotingToken  # noqa: E501
from swagger_server import util

from src.auth.jwt import decode_token, generate_token


def app_create_user(body=None):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: New user info to be added.
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()  # noqa: E501

    uid = db.create_user(User.from_dict(body))
    if uid:
        print('uid', uid)
        token = generate_token(uid)
        return {"jwt_token": token}
    else:
        return 'Account already exists', 409


def get_user():  # noqa: E501
    """Get user info

     # noqa: E501


    :rtype: InlineResponse2001
    """

    token = connexion.request.headers["Authorization"].split()[1]
    token_info = decode_token(token)
    user = db.get_user(token_info['uid'])
    return user if user else 'Not found', 404


def get_voting_token():  # noqa: E501
    """Get token used to vote

     # noqa: E501


    :rtype: VotingToken
    """
    return 'do some magic!'


def remove_user():  # noqa: E501
    """Remove user from service. Only a user can remove himself, hence the user is infered from the JWT

     # noqa: E501


    :rtype: None
    """

    # Requires a procedure

    return 'do some magic!'


def update_user(body=None):  # noqa: E501
    """Update user info

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
        body = User.from_dict(connexion.request.get_json())  # noqa: E501

    # Requires a procedure
    return 'do some magic!'
