import time
import os
import six
from jose import jwt, JWTError
from werkzeug.exceptions import Unauthorized
from src.constants_enums.obj_keys import JwtTokenKeys

JWT_ISSUER = os.getenv('POLLINATION_URL')
JWT_SECRET = os.getenv('AUTH_SECRET')
JWT_LIFETIME_SECONDS = 3600
JWT_ALGORITHM = 'HS256'


def generate_token(user_id):
    """
    Generate a JWT from a given user_id.
    """
    timestamp = _current_timestamp()
    payload = {
        JwtTokenKeys.ISSUER: JWT_ISSUER,
        JwtTokenKeys.TIMESTAMP: int(timestamp),
        JwtTokenKeys.EXPIRATION: int(timestamp + JWT_LIFETIME_SECONDS),
        JwtTokenKeys.UID: str(user_id),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    """
    Decode a JWT into object.

    :throws: Unauthorized exception if invalid token
    """
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def _current_timestamp() -> int:
    return int(time.time())

