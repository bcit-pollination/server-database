from src.email.sendgrid_email import send_registration_email
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from src.auth.jwt import decode_token
import src.db.mysql_interface as db
from src.constants_enums.obj_keys import *
from src.constants_enums.privileges import PrivilegeLevels


def accept_org_invite(encrypted_data):  # noqa: E501
    """Accept invitation user to org

    Use this to invite user to org # noqa: E501

    :param encrypted_data: 
    :type encrypted_data: str

    :rtype: None
    """
    new_user = decode_token(encrypted_data)
    change_user_privilege({
        OrgInfoKeys.PRIVILEGE: PrivilegeLevels.INVITEE,
        OrgInfoKeys.ORG_ID: new_user[OrgInfoKeys.ORG_ID],
        UserInfoKeys.UID: new_user[UserInfoKeys.UID]
    })
    return None


def change_user_privilege(body):  # noqa: E501
    """Change user privileges

    user privileges are:&lt;br&gt; - 0 :&#x3D; invited&lt;br&gt; - 1 :&#x3D; member&lt;br&gt; - 2 :&#x3D; admin&lt;br&gt; - 3 :&#x3D; owner  # noqa: E501

    :param body: Information about the user to have the privileges changed
    :type body: dict | bytes

    :rtype: None
    """
    # TODO change user priv
    uid = body[UserInfoKeys.UID]
    privilege = body[OrgInfoKeys.PRIVILEGE]
    org_id = body[OrgInfoKeys.ORG_ID]
    db.update_privilege(uid, org_id, privilege)
    return None


def get_org_users(org_id):  # noqa: E501
    """Fetch org users

    Get all users # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: InlineResponse2003
    """
    org_users = db.get_users_from_org(org_id)
    return org_users


def remove_org_user(body):  # noqa: E501
    """Kick user from org

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    change_user_privilege({
        OrgInfoKeys.PRIVILEGE: PrivilegeLevels.REMOVED,
        OrgInfoKeys.ORG_ID: body[OrgInfoKeys.ORG_ID],
        UserInfoKeys.UID: body[UserInfoKeys.UID]
    })
    return None


def org_invite_user(body):  # noqa: E501
    """Add user to org

    Use this to invite user to org # noqa: E501

    :param body: A list of info for users to be invited
    :type body: dict | bytes

    :rtype: None
    """
    users_to_invite = body[OrgInfoKeys.INVITES]
    org_id = body[OrgInfoKeys.ORG_ID]
    org_name = db.get_organization(org_id)[OrgInfoKeys.NAME]
    for user in users_to_invite:
        email = user[UserInfoKeys.EMAIL]
        user_org_id = user[OrgInfoKeys.USER_ORG_ID]
        db.invite_user(email, user_org_id, org_id)
        send_registration_email(org_name, org_id, email)
    return None
