import connexion
import six

from server.swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from server.swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from server.swagger_server.models.voting_token import VotingToken  # noqa: E501
from server.swagger_server import util
from werkzeug.exceptions import BadRequest
import server.src.obj_keys as obj_keys
import server.src.db.mysql_interface as db
from server.swagger_server.models.user import User


def app_create_user(body=None):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: New user info to be added.
    :type body: dict | bytes

    :rtype: InlineResponse200
    """

    body = object.from_dict(connexion.request.get_json())
    db.create_user(
            dob=body[obj_keys.DOB],
            first_name=body[obj_keys.FIRST_NAME],
            last_name=body[obj_keys.LAST_NAME],
            email=body[obj_keys.EMAIL],
            password=body[obj_keys.PASSWORD]
            )
    # noqa: E501
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
