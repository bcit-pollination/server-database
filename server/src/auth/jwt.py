import time

import six
from jose import jwt, JWTError
from werkzeug.exceptions import Unauthorized

JWT_ISSUER = 'pollination.live'
JWT_SECRET = 'l4GrQUps9mxmwgKVVvtDHBi6f86ZdQplBcNEmWyDt9KGYAoNUndskgMUEnQoxIgs'
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = 'HS256'

JWT_TIMESTAMP_KEY = "iat"
JWT_EXPIRATION_KEY = "exp"
JWT_UID_KEY = "uid"

def generate_token(user_id):
    """
    Generate a JWT from a given user_id.
    """
    timestamp = _current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        JWT_TIMESTAMP_KEY: int(timestamp),
        JWT_EXPIRATION_KEY: int(timestamp + JWT_LIFETIME_SECONDS),
        JWT_UID_KEY: str(user_id),
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

