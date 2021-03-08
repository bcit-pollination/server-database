from werkzeug.exceptions import NotFound

import src.db.mysql_interface as db
from src.constants_enums.obj_keys import ElectionKeys, QuestionKeys
from swagger_server.models import Option, Question, Election
from swagger_server.models.option_results import OptionResults


def get_question_options(question_id):
    options = db.get_question_opt(question_id)
    if options is None or len(options) == 0:
        raise NotFound(f"No question options found question_id: {question_id}")
    option_model_list = []
    total_votes_cast = 0
    for option in options:
        total_votes_cast += option[3]
        option_model_list.append(OptionResults(option[0], option[1], option[2], 0))
    if total_votes_cast == 0:
        return option_model_list
    for option_model in option_model_list:
        option_model.vote_proportion_percent = option_model.total_votes_for / total_votes_cast * 100
    return option_model_list


def get_election_questions(election_id):
    questions = db.get_election_questions(election_id)
    if questions is None or len(questions) == 0:
        raise NotFound("No questions found for election")
    question_models = []
    for question in questions:
        question_id = question[0]
        question_description = question[1]
        max_selection_count = question[2]
        options = get_question_options(question_id)
        question_models.append(Question(question_id, question_description, election_id, max_selection_count, options))
    return question_models


def get_election_with_results(election_id):
    """Get election info

        Get one election # noqa: E501

        :param election_id: The id of the election
        :type election_id: int

        :rtype: Election
        """
    election = db.get_election(election_id)
    if election is None:
        raise NotFound("Election was not found")
    org_id = election[1]
    election_description = election[2]
    start_time = election[3]
    end_time = election[4]
    anonymous = election[5] == 1
    public_results = election[6] == 1
    verified = election[7] == 1
    questions = get_election_questions(election_id)
    election_model = Election(election_description, election_id, org_id, start_time, end_time, anonymous, verified,
                              public_results, questions)
    return election_model


def get_questions_and_options(election_id):
    questions_and_options = db.get_questions_and_options(election_id)
    if questions_and_options is None:
        raise NotFound("No data found for election")
    questions_info = {}
    for question_and_option in questions_and_options:
        question_id = question_and_option[0]
        if question_id not in questions_info:
            questions_info[question_id] = {}
        questions_info[question_id][QuestionKeys.MIN_SELECTION_COUNT] = question_and_option[2]
        questions_info[question_id][QuestionKeys.MAX_SELECTION_COUNT] = question_and_option[3]
        if QuestionKeys.OPTIONS not in questions_info[question_id]:
            questions_info[question_id][QuestionKeys.OPTIONS] = set()
        questions_info[question_id][QuestionKeys.OPTIONS].add(question_and_option[4])
    return questions_info


def get_election_start_end(election_id):
    election = db.get_election(election_id)
    if election is None:
        raise NotFound("Election was not found")
    if election is None:
        raise NotFound("Election was not found")
    return election[3], election[4]
