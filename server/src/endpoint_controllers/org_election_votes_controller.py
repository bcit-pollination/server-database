import connexion
import six
from werkzeug.exceptions import InternalServerError, BadRequest

from src.constants_enums.datetime_format import DateFormats
from src.constants_enums.obj_keys import ElectionKeys, VoteKeys, QuestionKeys, UserInfoKeys
from src.db.rollbacks import rollback_add_votes
from swagger_server import util
from swagger_server.models import Vote, Choice
from src.utils.date_utils import compare_date_strings, TimeRelations
import src.db.mysql_interface as db
from src.utils.logging import Logger
from src.db.org_election_query_helper import get_questions_and_options, get_election_start_end


def log_vote(vote, reason, logger):
    log_string = f"\nREJECTED VOTE: \n" \
                 f"Reason: {reason}\n" \
                 f"Vote: {vote}"
    logger.add_entry(log_string)


def latest_pass_discriminator(vote, **kwargs):
    """
    Discriminate based on time_stamp

    :returns: True if vote passes discrimination, else False
    """
    votes_seen = kwargs["votes_seen"]
    if vote.voting_token not in votes_seen:
        return True
    other_vote = votes_seen[vote.voting_token]
    try:
        date_delta = compare_date_strings(vote.time_stamp, other_vote.time_stamp, DateFormats.ELECTION_TIME_FORMAT)
    except ValueError:
        raise BadRequest("Invalid date format")
    if date_delta == TimeRelations.LFT_LATER:
        return True
    return False


def selection_count_discriminator(vote, **kwargs):
    questions_info = kwargs["questions_info"]
    choices_per_question = {}
    for choice in vote.choices:
        if choice.question_id not in choices_per_question:
            choices_per_question[choice.question_id] = []
        choices_per_question[choice.question_id].append(choice.option_id)
    for question_id, choices_made in choices_per_question.items():
        # TODO questions_info[question_id][QuestionKeys.MIN_SELECTION_COUNT]
        if not (1 <= len(choices_made) <= questions_info[question_id][QuestionKeys.MAX_SELECTION_COUNT]):
            return False
    return True


def possible_options_discriminator(vote, **kwargs):
    questions_info = kwargs["questions_info"]
    for choice in vote.choices:
        if choice.question_id not in questions_info:
            return False
        possible_option_ids = questions_info[choice.question_id][QuestionKeys.OPTIONS]
        if choice.option_id not in possible_option_ids:
            return False
    return True


def valid_voting_token_discriminator(vote, **kwargs):
    election_id = kwargs["election_id"]
    return True


def within_election_timeframe_discriminator(vote, **kwargs):
    vote_time_stamp_string = vote.time_stamp
    election_start_end = kwargs['election_start_end']
    election_start_time_relation = compare_date_strings(vote_time_stamp_string, election_start_end[0],
                                                        DateFormats.ELECTION_TIME_FORMAT)
    election_end_time_relation = compare_date_strings(vote_time_stamp_string, election_start_end[1],
                                                      DateFormats.ELECTION_TIME_FORMAT)

    return election_start_time_relation != TimeRelations.LFT_EARLIER \
        and election_end_time_relation != TimeRelations.LFT_LATER


def decorate_discriminator_with_logger(discriminator, msg, logger):
    def _(vote, **kwargs):
        passed = discriminator(vote, **kwargs)
        if not passed:
            log_vote(vote, msg, logger)
        return passed

    return _


def get_latest_pass_discriminator(logger):
    return decorate_discriminator_with_logger(latest_pass_discriminator, "voting_token_conflict", logger)


def get_selection_count_discriminator(logger):
    return decorate_discriminator_with_logger(selection_count_discriminator, "selection count conflict", logger)


def get_possible_options_discriminator(logger):
    return decorate_discriminator_with_logger(possible_options_discriminator, "Option chosen not a possible option",
                                              logger)


def get_valid_voting_token_discriminator(logger):
    return decorate_discriminator_with_logger(valid_voting_token_discriminator,
                                              "Invalid voting_token or voting_token "
                                              "has no right to vote in this election",
                                              logger)


def get_within_election_timeframe_discriminator(logger):
    return decorate_discriminator_with_logger(within_election_timeframe_discriminator,
                                              "Vote was not cast within election time frame", logger)



def discriminate_vote(vote, discriminator_list, **kwargs):
    """
    Examine vote using a list of discriminators
    """
    for discriminator in discriminator_list:
        if not discriminator(vote, **kwargs):
            return False
    return True


def filter_votes(vote_list, discriminator_list, **kwargs):
    votes_seen = {}
    for vote in vote_list:
        if discriminate_vote(vote, discriminator_list, votes_seen=votes_seen, **kwargs):
            votes_seen[vote.voting_token] = vote
    return list(votes_seen.values())


def add_vote(vote, election_id):
    voting_token = vote.voting_token
    timestamp = vote.time_stamp
    election_id = election_id
    vote_id_tuple = db.add_vote(voting_token, timestamp, election_id)
    if vote_id_tuple is None:
        raise InternalServerError("DB error adding vote. Rolling back")
    vote_id = vote_id_tuple[0]
    for choice in vote.choices:
        option_id = choice.option_id
        choice_id_tuple = db.add_choice(vote_id, option_id)
        if choice_id_tuple is None:
            raise InternalServerError("DB error adding vote. Rolling back")
    return vote_id


def add_election_votes(vote_list, election_id):
    votes_added_ids = []
    for vote in vote_list:
        try:
            add_vote(vote, election_id)
        except Exception as e:
            rollback_add_votes(votes_added_ids)
            raise e


def build_vote_models(vote_dicts):
    votes = []
    for vote in vote_dicts:
        choices = []
        for choice in vote[VoteKeys.CHOICES]:
            choices.append(Choice(choice[QuestionKeys.QUESTION_ID], choice[QuestionKeys.OPTION_ID]))
        votes.append(Vote(vote[VoteKeys.VOTER_FIRST_NAME], vote[VoteKeys.VOTER_LAST_NAME],
                          vote[UserInfoKeys.VOTING_TOKEN], choices, vote[VoteKeys.TIME_STAMP],
                          vote[VoteKeys.LOCATION]))
    return votes


def upload_election_votes(body):  # noqa: E501
    """Create/Update election results

    Create/Update election results. Each call will add a new versioned entry for security purposes.  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    vote_dicts = body[VoteKeys.VOTES_CAST]
    election_id = body[ElectionKeys.ELECTION_ID]
    election_start_end = get_election_start_end(election_id)
    unfiltered_votes = build_vote_models(vote_dicts)
    questions_info = get_questions_and_options(election_id)
    logger = Logger(f"election_{election_id}_voting_log")
    filtered_votes = filter_votes(unfiltered_votes, [get_latest_pass_discriminator(logger),
                                                     get_possible_options_discriminator(logger),
                                                     get_selection_count_discriminator(logger),
                                                     get_valid_voting_token_discriminator(logger),
                                                     get_within_election_timeframe_discriminator(logger)],
                                  questions_info=questions_info,
                                  election_id=election_id,
                                  election_start_end=election_start_end)
    # add_election_votes(filtered_votes, election_id)
    print(filtered_votes)
    return None
