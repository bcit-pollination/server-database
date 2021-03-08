class PROCEDURE:
    """
    List of available procedures available in the Pollination MySql database.

    https://docs.google.com/document/d/1ny0d3P38eVzZHJG2Odj71t52vtQhlIupdYiwLjgoMec/edit
    """
    # name                    = proc_name                   # procedure parameters
    LOGINUSER                 = 'LoginUser'                 # email, password
    CREATEUSER                = 'CreateUser'                # first_name, last_name, email, dob, password, voting_token
    CREATEORG                 = 'CreateOrg'                 # user_id, org_name, user_org_id, verifier_password
    ENROLLUSER                = 'EnrollUser'                # user_id, user_org_id, email
    GETUSER                   = 'GetUser'                   # user_id
    GETUSERORGANIZATIONS      = 'GetUserOrgListInfo'        # user_id
    GETUSERELECTIONS          = 'GetUserElections'          # user_id
    GETORGANIZATIONUSERS      = 'GetUsersFromOrg'           # org_id
    GETUSERELECTIONSALTERNATE = 'GetElectionsAlternate'     # user_id
    UPDATEUSER                = 'UpdateUser'                # user_id, first_name, last_name, email, password
    DEACTIVATEUSER            = 'DeactivateUser'            # user_id
    GETUSERTOKEN              = 'GetUserToken'              # user_id
    GETUSERORGLIST            = 'GetUserOrgListInfo'        # user_id
    GETORGANIZATION           = 'GetOrg'                    # org_id
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
    GETELECTIONLISTORG        = 'GetOrgElections'           # org_id
    GETELECTIONLISTUSER       = 'GetElectionListUser'       # user_id
    GETINDIVIDUALVOTES        = 'GetUserVotes'              # election_id
    GETELECTIONSATLERNATE     = 'GetElectionsAlternate'     # user_id
    GETQUESTIONOPT            = 'GetQuestionOptions'        # question_id
    GETELECTIONQUESTIONS      = 'GetQuestions'              # election_id
    GETPUBLICELECTIONS        = 'GetPublicElections'        # NOTHING
    ADDQUESTION               = 'AddQuestion'               # election_id, description
    DROPQUESTION              = 'DeleteQuestion'            # question_id
    UPDATEQUESTION            = 'UpdateQuestion'            # question_id, description
    UPDATEQUESTIONOPT         = 'UpdateOption'              # option_id, description
    ADDOPT                    = 'AddOption'                 # opt_id
    DELETEOPTION              = 'DeleteOption'              # opt_id
    UPDATEOPT                 = 'UpdateOpt'                 # opt_id, description
    GETPRIVILEGE              = 'GetPrivilege'              # org_id, user_id
    GETIDVT                   = 'GetIdVt'                   # election_id
    ADDVOTE                   = 'AddVote'                   # voting_token, time_stamp, election_id
    ADDCHOICE                 = 'AddChoice'                 # vote_id, opt_id
    GETOWNERORGINFO           = 'GetOwnerOrgInfo'           # uid
    GETQUESTIONSANDOPTIONS    = 'GetQuestionsAndOptions'    # election_id
    ISELIGIBLE                = 'IsEligible'                # voting_token, election_id
