import connexion
import six

from src.utils.logging import with_exception_log
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server import util
from src.endpoint_controllers import org_users_controller as ctl


@with_exception_log
def accept_org_invite(encrypted_data):  # noqa: E501
    """Accept invitation user to org

    Use this to invite user to org # noqa: E501

    :param encrypted_data: 
    :type encrypted_data: str

    :rtype: None
    """
    return ctl.accept_org_invite(encrypted_data)


@with_exception_log
def change_user_privilege(body, token_info):  # noqa
    """Change user privileges

    user privileges are:&lt;br&gt; 0 :&#x3D; removed&lt;br&gt; 1 :&#x3D; invited&lt;br&gt; 2 :&#x3D; member&lt;br&gt; 3 :&#x3D; admin&lt;br&gt; 4 :&#x3D; owner  # noqa: E501

    :param body: Information about the user to have the privileges changed
    :type body: dict | bytes

    :rtype: None
    """
    return ctl.change_user_privilege(body, token_info)


@with_exception_log
def get_org_users(org_id, min_privilege_level=1):  # noqa: E501
    """Fetch org users

    Get all users # noqa: E501

    :param org_id: The id of the org
    :type org_id: int
    :param min_privilege_level: The minimum privilege level a user must have in order to be fetched
    :type min_privilege_level: int

    :rtype: InlineResponse2003
    """
    return ctl.get_org_users(org_id, min_privilege_level)


@with_exception_log
def org_invite_user(body, token_info):  # noqa: E501
    """Add user to org

    Use this to invite user to org # noqa: E501

    :param body: A list of info for users to be invited
    :type body: dict | bytes

    :rtype: None
    """
    return ctl.org_invite_user(body, token_info)


@with_exception_log
def remove_org_user(body, token_info):  # noqa
    """Remove user from org

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    return ctl.remove_org_user(body, token_info)
