import src.db.mysql_interface as db


def rollback_create_election(election_id, question_id_list, option_id_list):
    for option_id in option_id_list:
        db.remove_question_opt(option_id)
    for question_id in question_id_list:
        db.remove_question(question_id)
    db.remove_election(election_id)


def rollback_add_votes(vote_ids):
    pass
