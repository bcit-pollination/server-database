import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.voting_token import VotingToken  # noqa: E501
from swagger_server import util


def app_create_user(body=None):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: New user info to be added.
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_user():  # noqa: E501
    """Get user info

     # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'


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
    return 'do some magic!'


def update_user(body=None):  # noqa: E501
    """Update user info

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
