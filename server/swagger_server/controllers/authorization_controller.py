from typing import List
import connexion
import server.src.auth.authorization_control as auth_ctl

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_admin(token):
    return auth_ctl.check_admin(token)


def check_member(token):
    return auth_ctl.check_member(token)


def check_owner(token):
    return auth_ctl.check_owner(token)


def check_user(token):
    return auth_ctl.check_user(token)
