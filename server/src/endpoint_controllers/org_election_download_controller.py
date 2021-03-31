
import connexion
import six

from src.constants_enums.obj_keys import OrgInfoKeys, UserInfoKeys
from src.constants_enums.privileges import PrivilegeLevels
from swagger_server.models import VotingUser
from swagger_server.models.inline_response2007 import InlineResponse2007  # noqa: E501
from swagger_server import util
from src.endpoint_controllers.org_users_controller import get_org_users
from src.endpoint_controllers.org_controller import get_verifier_password
from src.endpoint_controllers.org_elections_controller import get_election
from src.endpoint_controllers.user_controller import get_voting_token


def prepare_voting_users(user_list):
    voting_users = []
    for user in user_list:
        voting_token = get_voting_token({UserInfoKeys.UID: user.uid})
        voting_users.append(VotingUser(voting_token.voting_token, user.user_org_id))
    return voting_users


def download_voting_package(election_id):  # noqa: E501
    """Download main RPI election package

    Gives the necessary information for a completely standalone voting process. The information included is:   - Complete voter list, including their respective identification within the org and voting token   - Ballot, including the election details and questions   - List of locations   - Verifier password  # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: InlineResponse2007
    """
    election = get_election(election_id)
    verifier_password = get_verifier_password({OrgInfoKeys.ORG_ID: election.org_id})
    voter_list = get_org_users(election.org_id, PrivilegeLevels.MEMBER)
    voting_users = prepare_voting_users(voter_list.users)
    election_package = InlineResponse2007(verifier_password.verifier_password, voting_users, election)
    return election_package
