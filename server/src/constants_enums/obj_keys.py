# REQUEST BODY

class UserInfoKeys:
    UID = "uid"
    DOB = "dob"
    EMAIL = "email"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    PASSWORD = "password"
    VOTING_TOKEN = "voting_token"


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
    ELECTION_DESCRIPTION = "election_description"
    END_TIME = "end_time"
    START_TIME = "start_time"
    ANONYMOUS = "anonymous"
    VERIFIED = "verified"
    PUBLIC_RESULTS = "public_results"
    QUESTIONS = "questions"


class QuestionKeys:
    MAX_SELECTION_COUNT = "max_selection_count"
    MIN_SELECTION_COUNT = "min_selection_count"
    OPTIONS = "options"
    OPTION_DESCRIPTION = "option_description"
    QUESTION_ID = "question_id"
    OPTION_ID = "option_id"
    QUESTION_DESCRIPTION = "question_description"
    ORDERED_CHOICES = "ordered_choices"
    ORDER_POSITION = "order_position"


class VoteKeys:
    TIME_STAMP = "time_stamp"
    VOTES_CAST = "votes_cast"
    CHOICES = "choices"
    LOCATION = "location"
    VOTER_FIRST_NAME = "voter_first_name"
    VOTER_LAST_NAME = "voter_last_name"
    ORDER_POSITION = "order_position"
