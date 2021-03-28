from werkzeug.exceptions import NotFound, Conflict, BadRequest

from src.email.sendgrid_email import send_registration_email, decode_user_info
from swagger_server.models import OrgUser
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
    print(encrypted_data)
    new_user = decode_user_info(encrypted_data)
    uid_tuple = db.get_user_id(new_user[UserInfoKeys.EMAIL])
    if not uid_tuple or len(uid_tuple) == 0:
        # TODO we probably want to redirect to home page
        raise NotFound("No user associated with that email")
    org_user_info_tuple = db.get_organization(new_user[OrgInfoKeys.ORG_ID], uid_tuple[0])
    if org_user_info_tuple is None or len(org_user_info_tuple) == 0:
        raise NotFound("Cannot find the organization to accept invite")
    if PrivilegeLevels.INVITEE != org_user_info_tuple[2]:
        raise Conflict("You can only accept invitations if you are invited")
    db.update_privilege(uid_tuple[0], new_user[OrgInfoKeys.ORG_ID], PrivilegeLevels.MEMBER)

    return "invitation accepted", 301, {'Location': 'https://pollination.live'}


def change_user_privilege(body, token_info):  # noqa
    """Change user privileges

    user privileges are:&lt;br&gt; - 0 :&#x3D; invited&lt;br&gt; - 1 :&#x3D; member&lt;br&gt; - 2 :&#x3D; admin&lt;br&gt; - 3 :&#x3D; owner  # noqa: E501

    :param body: Information about the user to have the privileges changed
    :type body: dict | bytes

    :rtype: None
    """
    uid = body[UserInfoKeys.UID]
    privilege = body[OrgInfoKeys.PRIVILEGE]
    org_id = body[OrgInfoKeys.ORG_ID]
    db.update_privilege(uid, org_id, privilege)
    return None


def get_org_users(org_id, privilege_level):  # noqa: E501
    """Fetch org users

    Get all users # noqa: E501

    :rtype: InlineResponse2003
    """
    if org_id is None or privilege_level is None:
        raise BadRequest("must provide org_id and privilage_level in url params")
    org_users = db.get_users_from_org(org_id, privilege_level)
    if org_users is None:
        raise NotFound("No such organization")
    org_user_models = []
    for org_user in org_users:
        uid = org_user[0]
        first_name = org_user[1]
        last_name = org_user[2]
        email = org_user[3]
        dob = org_user[4]
        privilege = org_user[5]
        user_org_id = org_user[6]
        org_user_models.append(OrgUser(uid, first_name, last_name, email, dob, privilege=privilege,
                                       user_org_id=user_org_id))
    return InlineResponse2003(org_user_models)


def remove_org_user(body, token_info):  # noqa
    """Kick user from org

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    change_user_privilege({
        OrgInfoKeys.PRIVILEGE: PrivilegeLevels.REMOVED,
        UserInfoKeys.UID: body[UserInfoKeys.UID]
    }, token_info)
    return None


def org_invite_user(body, token_info):  # noqa
    """Add user to org

    Use this to invite user to org # noqa: E501

    :param body: A list of info for users to be invited
    :type body: dict | bytes

    :rtype: None
    """
    users_to_invite = body[OrgInfoKeys.INVITES]
    org_id = body[OrgInfoKeys.ORG_ID]
    org_name_tuple = db.get_organization(org_id, token_info[JwtTokenKeys.UID])
    org_name = org_name_tuple[1]
    for user in users_to_invite:
        email = user[UserInfoKeys.EMAIL]
        user_org_id = user[OrgInfoKeys.USER_ORG_ID]
        db.invite_user(email, user_org_id, org_id)
        send_registration_email(org_name, org_id, email)
    return None
