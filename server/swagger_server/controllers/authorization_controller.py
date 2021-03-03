from typing import List
from src.auth import authorization_control

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_admin(token):
    return authorization_control.check_admin(token)


def check_member(token):
    return authorization_control.check_member(token)


def check_owner(token):
    return authorization_control.check_owner(token)


def check_user(token):
    return authorization_control.check_user(token)
