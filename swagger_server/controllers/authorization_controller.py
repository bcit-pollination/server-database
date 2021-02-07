from werkzeug.exceptions import Unauthorized

from src.auth.jwt import decode_token

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_jwt(token):
    try:
        return decode_token(token)
    except Unauthorized as not_auth:
        return None
