# REQUEST BODY

class UserInfoKeys:
    UID = "uid"
    DOB = "dob"
    EMAIL = "email"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    PASSWORD = "password"


class OrgInfoKeys:
    ORG_ID = "org_id"


class LoginKeys:
    EMAIL = UserInfoKeys.EMAIL
    PASSWORD = UserInfoKeys.PASSWORD


class JwtTokenKeys:
    ISSUER = "iss"
    TIMESTAMP = "iat"
    EXPIRATION = "exp"
    UID = UserInfoKeys.UID
