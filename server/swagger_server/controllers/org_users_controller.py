import connexion
import six

from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server import util


def accept_org_invite(encrypted_data):  # noqa: E501
    """Accept invitation user to org

    Use this to invite user to org # noqa: E501

    :param encrypted_data: 
    :type encrypted_data: str

    :rtype: None
    """
    return 'do some magic!'


def change_user_privilege(body):  # noqa: E501
    """Change user privileges

    user privileges are:&lt;br&gt; - 0 :&#x3D; invited&lt;br&gt; - 1 :&#x3D; member&lt;br&gt; - 2 :&#x3D; admin&lt;br&gt; - 3 :&#x3D; owner  # noqa: E501

    :param body: Information about the user to have the privileges changed
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_org_users(org_id):  # noqa: E501
    """Fetch org users

    Get all users # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: InlineResponse2005
    """
    return 'do some magic!'


def kick_org_user(body):  # noqa: E501
    """Kick user from org

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def org_invite_user(body):  # noqa: E501
    """Add user to org

    Use this to invite user to org # noqa: E501

    :param body: A list of info for users to be invited
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
