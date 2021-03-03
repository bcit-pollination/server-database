import connexion
import six

from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server import util
from src.endpoint_controllers import org_users_controller


def accept_org_invite(encrypted_data):  # noqa: E501
    """Accept invitation user to org

    Use this to invite user to org # noqa: E501

    :param encrypted_data: 
    :type encrypted_data: str

    :rtype: None
    """
    return org_users_controller.accept_org_invite(encrypted_data)


def change_user_privilege(body):  # noqa: E501
    """Change user privileges

    user privileges are:&lt;br&gt; - 0 :&#x3D; invited&lt;br&gt; - 1 :&#x3D; member&lt;br&gt; - 2 :&#x3D; admin&lt;br&gt; - 3 :&#x3D; owner  # noqa: E501

    :param body: Information about the user to have the privileges changed
    :type body: dict | bytes

    :rtype: None
    """
    return org_users_controller.change_user_privilege(body)


def get_org_users(org_id):  # noqa: E501
    """Fetch org users

    Get all users # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: InlineResponse2003
    """
    return org_users_controller.get_org_users(org_id)


def kick_org_user(body):  # noqa: E501
    """Kick user from org

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    return org_users_controller.remove_org_user(body)


def org_invite_user(body):  # noqa: E501
    """Add user to org

    Use this to invite user to org # noqa: E501

    :param body: A list of info for users to be invited
    :type body: dict | bytes

    :rtype: None
    """
    return org_users_controller.org_invite_user(body)
