from typing import List
import src.auth.authorization_control as ctl
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_admin_with_election_id(token):
    return ctl.check_admin_with_election_id(token)


def check_admin_with_org_id(token):
    return ctl.check_admin_with_org_id(token)


def check_member_with_election_id(token):
    return ctl.check_member_with_election_id(token)


def check_member_with_org_id(token):
    return ctl.check_member_with_org_id(token)


def check_owner(token):
    return ctl.check_owner(token)


def check_user(token):
    return ctl.check_user(token)
