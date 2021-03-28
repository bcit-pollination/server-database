import hashlib
import secrets

SALT_LEN = 32


def hash_password(password, salt):
    encoded_password = password.encode('utf-8')
    key = hashlib.pbkdf2_hmac('sha256', encoded_password, salt, 150000)
    return key


def get_hash(password):
    encoded_salt = secrets.token_urlsafe(SALT_LEN).encode('utf-8')[:SALT_LEN]
    return encoded_salt + hash_password(password, encoded_salt)


def check_password(password_candidate, password_hash):
    salt = password_hash[:SALT_LEN]
    phash = password_hash[SALT_LEN:]
    candidate_hash = hash_password(password_candidate, salt)
    return candidate_hash == phash
