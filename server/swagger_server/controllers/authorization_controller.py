from typing import List
from src.auth import authorization_control as ctl

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_admin(token):
    return ctl.check_admin(token)


def check_member(token):
    return ctl.check_member(token)


def check_owner(token):
    return ctl.check_owner(token)


def check_user(token):
    return ctl.check_user(token)
