import connexion
import six
from werkzeug.exceptions import BadRequest, NotFound

from src.constants_enums.obj_keys import *
from src.utils.date_utils import compare_date_strings, TimeRelations
from swagger_server.models.election import Election  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server import util
import src.db.mysql_interface as db
from src.db.rollbacks import rollback_create_election
from src.db.org_election_query_helper import *
from src.constants_enums.datetime_format import DateFormats


def create_election(body):  # noqa: E501
    """Create election

    Create election # noqa: E501

    :param body: Election ID is not required to POST
    :type body: dict | bytes

    :rtype: InlineResponse2005
    """

    start_time = body[ElectionKeys.START_TIME]
    end_time = body[ElectionKeys.END_TIME]
    anonymous = body[ElectionKeys.ANONYMOUS]
    verified = body[ElectionKeys.VERIFIED]
    public_results = body[ElectionKeys.PUBLIC_RESULTS]
    questions = body[ElectionKeys.QUESTIONS]
    election_description = body[ElectionKeys.ELECTION_DESCRIPTION]
    org_id = body[OrgInfoKeys.ORG_ID]

    try:
        start_end_delta = compare_date_strings(start_time, end_time, DateFormats.ELECTION_TIME_FORMAT)
    except ValueError:
        raise BadRequest("Incorrect date format")

    if not start_end_delta == TimeRelations.LFT_EARLIER:
        raise BadRequest("End time must strictly be later than start time")

    if len(questions) < 1:
        raise BadRequest("Elections must have at least one question")

    election_id = db.create_election(org_id, election_description, start_time, end_time, anonymous, public_results,
                                     verified)

    add_questions(election_id, questions)
    return InlineResponse2005(election_id[0])


def add_questions(election_id, questions):
    question_id_list = []
    option_id_list = []
    for question in questions:
        question_description = question[QuestionKeys.QUESTION_DESCRIPTION]
        max_selection_count = question[QuestionKeys.MAX_SELECTION_COUNT]
        min_selection_count = question[QuestionKeys.MIN_SELECTION_COUNT]
        prioritized_choices = question[QuestionKeys.ORDERED_CHOICES]
        if max_selection_count < 1:
            rollback_create_election(election_id, question_id_list, option_id_list)
            raise BadRequest(
                "You must be able to choose at least one option in every question: max_selection_count < 1")
        try:
            question_id = db.add_question(election_id, question_description, min_selection_count, max_selection_count,
                                          prioritized_choices)
        except Exception as e:
            rollback_create_election(election_id, question_id_list, option_id_list)
            raise e
        question_id_list.append(question_id)
        if len(question[QuestionKeys.OPTIONS]) < 2:
            rollback_create_election(election_id, question_id_list, option_id_list)
            raise BadRequest("Every question must contain at least 2 options")
        add_options(election_id, question, question_id, question_id_list, option_id_list)


def add_options(election_id, question, question_id, question_id_list, option_id_list):
    for option in question[QuestionKeys.OPTIONS]:
        option_description = option[QuestionKeys.OPTION_DESCRIPTION]
        try:
            option_id = db.add_question_opt(question_id, option_description)
        except Exception as e:
            rollback_create_election(election_id, question_id_list, option_id_list)
            raise e
        option_id_list.append(option_id)


def delete_election(election_id):  # noqa: E501
    """Delete election

    Elections can only be deleted before they have commenced.  # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: None
    """
    # db.remove_election(election_id)
    return 'do some magic!'


def get_election(election_id):  # noqa: E501
    """Get election info

    Get one election # noqa: E501

    :param election_id: The id of the election
    :type election_id: int

    :rtype: Election
    """
    election = get_election_with_results(election_id)
    for question in election.questions:
        new_options = []
        for option in question.options:
            new_options.append(Option(option.option_id, option.option_description))
        question.options = new_options
    return election


def get_election_list(org_id):  # noqa: E501
    """Get election info list

    Get list of elections for a given org # noqa: E501

    :param org_id: The id of the org
    :type org_id: int

    :rtype: InlineResponse2004
    """
    election_list_tuple = db.get_org_elections(org_id)
    parsed_elections = []
    for election in election_list_tuple:
        election_id = election[0]
        org_id = org_id
        description = election[2]
        start_time = election[3]
        end_time = election[4]
        anonymous = election[5] == 1
        verified = election[6] == 1
        public_results = election[7] == 1
        parsed_election = Election(description, election_id, org_id, start_time, end_time, anonymous, verified,
                                   public_results, [])
        parsed_elections.append(parsed_election)
    return InlineResponse2004(parsed_elections)


def update_election(body):  # noqa: E501
    """update election

    Update election. Elections can only be updated before they have commenced.  # noqa: E501

    :param body: Election ID is not required to POST
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Election.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
