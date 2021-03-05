# REQUEST BODY

class UserInfoKeys:
    UID = "uid"
    DOB = "dob"
    EMAIL = "email"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    PASSWORD = "password"


class OrgInfoKeys:
    NAME = "name"
    ORG_ID = "org_id"
    PRIVILEGE = "privilege"
    INVITES = "invites"
    USER_ORG_ID = "user_org_id"
    ORG_INFO = "org_info"
    VERIFIER_PASSWORD = "verifier_password"


class LoginKeys:
    EMAIL = UserInfoKeys.EMAIL
    PASSWORD = UserInfoKeys.PASSWORD


class JwtTokenKeys:
    ISSUER = "iss"
    TIMESTAMP = "iat"
    EXPIRATION = "exp"
    UID = UserInfoKeys.UID


class ElectionKeys:
    ELECTION_ID = "election_id"
