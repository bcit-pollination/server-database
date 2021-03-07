from src.endpoint_controllers import user_controller as ctl


def app_create_user(body):  # noqa: E501
    """Create user

     # noqa: E501

    :param body: New user info to be added.
    :type body: dict | bytes

    :rtype: InlineResponse200
    """

    return ctl.app_create_user(body)


def get_user(token_info):  # noqa: E501
    """Get user info

     # noqa: E501


    :rtype: User
    """
    return ctl.get_user(token_info)


def get_voting_token(token_info):  # noqa: E501
    """Get token used to vote

     # noqa: E501


    :rtype: VotingToken
    """
    return ctl.get_voting_token(token_info)


def remove_user(token_info):  # noqa: E501
    """Remove user from service. Only a user can remove himself, hence the user is inferred from the JWT

     # noqa: E501


    :rtype: None
    """
    return ctl.remove_user(token_info)
