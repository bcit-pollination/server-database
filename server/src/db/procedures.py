class PROCEDURE:
    """
    List of available procedures available in the Pollination MySql database.
    """
    # name                    = proc_name                   # procedure parameters
    LOGINUSER                 = 'LoginUser'                 # email, password
    CREATEUSER                = 'CreateUser'                # first_name, last_name, email, dob, password, voting_token
    CREATEORG                 = 'CreateOrg'                 # user_id, org_name, user_org_id, verifier_password
    ENROLLUSER                = 'EnrollUser'                # user_id, user_org_id, email
    GETUSER                   = 'GetUser'                   # user_id
    GETUSERORGANIZATION       = 'GetUserOrganization'       # user_id
    GETUSERELECTIONS          = 'GetUserElections'          # user_id
    GETORGANIZATIONUSERS      = 'GetOrganizationUsers'      # org_id
    GETUSERELECTIONSALTERNATE = 'GetUserElectionsAlternate' # user_id
    UPDATEUSER                = 'UpdateUser'                # user_id, first_name, last_name, email, password
    DEACTIVATEUSER            = 'DeactivateUser'            # user_id
    GETUSERTOKEN              = 'GetUserToken'              # user_id
    GETORGANIZATIONS          = 'GetOrganizations'          # user_id
    GETORGANIZATION           = 'GetOrganization'           # org_id
    UPDATEORGANIZATION        = 'UpdateOrg'                 # org_id, org_name, verifier_password
    DISBANDORG                = 'DisbandOrg'                # org_id
    GETVERIFIERPASSWORD       = 'GetVerifierPassword'       # org_id
    GETUSERSFROMORG           = 'GetUsersFromOrg'           # org_id, privilege_level
    UPDATEPRIVILEGE           = 'UpdatePrivilege'           # user_id, org_id, privilege_level
    INVITEUSER                = 'InviteUser'                # user_id, org_id, user_org_id
    CREATEELECTION            = 'CreateElection'            # org_id, description, start_time, end_time, status, is_public, is_anonymous
    UPDATEELECTION            = 'UpdateElection'            # election_id, description, start_time, end_time, status, is_public, is_anonymous, questions
    DELETEELECTION            = 'DeleteElection'            # election_id
    GETELECTION               = 'GetElection'               # election_id
    GETELECTIONLISTORG        = 'GetElectionListOrg'        # org_id
    GETELECTIONLISTUSER       = 'GetElectionListUser'       # user_id
    GETINDIVIDUALVOTES        = 'GetIndividualVotes'        # election_id
    GETELECTIONSATLERNATE     = 'GetElectionsAlternate'     # user_id
    GETQUESTIONOPT            = 'GetQuestionOpt'            # question_id
    GETELECTIONQUESTIONS      = 'GetQuestions'      # election_id
    GETPUBLICELECTIONS        = 'GetPublicElections'        # NOTHING
    ADDQUESTION               = 'AddQuestion'               # election_id, description
    DROPQUESTION              = 'DropQuestion'              # question_id
    UPDATEQUESTION            = 'UpdateQuestion'            # question_id, description
    ADDOPT                    = 'AddOpt'                    # opt_id
    DROPOPT                   = 'DropOpt'                   # opt_id
    UPDATEOPT                 = 'UpdateOpt'                 # opt_id, description
    GETPRIVILEGE              = 'GetPrivilege'              # org_id, user_id
    GETIDVT                   = 'GetIdVt'                   # election_id
    CREATEVOTE                = 'CreateVote'                # voting_token, time_stamp, election_id
    CREATECHOICE              = 'CreateChoice'              # vote_id, opt_id

