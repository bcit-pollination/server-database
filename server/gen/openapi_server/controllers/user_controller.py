import connexion
import six

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.models.voting_token import VotingToken  # noqa: E501
from openapi_server import util


def app_create_user(unknown_base_type=None):  # noqa: E501
    """Create user

     # noqa: E501

    :param unknown_base_type: New user info to be added.
    :type unknown_base_type: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
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


def update_user(user=None):  # noqa: E501
    """Update user info

     # noqa: E501

    :param user: 
    :type user: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
