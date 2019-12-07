#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""User authentication module."""

from user import User


def authenticate(username, password):
    """Returns user object if exists, otherwise return None.
    :param username: string.
    :param password: string.
    :return: dictionary {'id': <id>, 'username': <username>, 'password': <password>}.
    """
    user = User.find_user_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    """Returns user id if exists, otherwise returns None.
    :param payload: dictionary.
    :return: user id.
    """
    user_id = payload['identity']
    return User.find_user_by_id(user_id)
