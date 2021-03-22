from typing import List
from src.auth import authorization_control as ctl
from src.utils.logging import with_exception_log

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


@with_exception_log
def check_admin(token):
    return ctl.check_admin(token)


@with_exception_log
def check_member(token):
    return ctl.check_member(token)


@with_exception_log
def check_owner(token):
    return ctl.check_owner(token)


@with_exception_log
def check_user(token):
    return ctl.check_user(token)
