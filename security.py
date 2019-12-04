#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""User authentication module."""

from user import User

# USERS = [{
#     'id': 1,
#     'username': 'john',
#     'password': '123'
# }, {
#     'id': 2,
#     'username': 'sarah',
#     'password': '456'
# }]

# USERID_MAPPING = {
#     1: {
#         'id': 1,
#         'username': 'john',
#         'password': '123'
#     },
#     2: {
#         'id': 2,
#         'username': 'sarah',
#         'password': '456'
#     }
# }

# USERNAME_MAPPING = {
#     'john': {
#         'id': 1,
#         'username': 'john',
#         'password': '123'
#     },
#     'sarah': {
#         'id': 2,
#         'username': 'sarah',
#         'password': '456'
#     }
# }

USERS = [User(1, 'john', '1357'), User(2, 'sarah', '2468')]
USERID_MAPPING = {u.id: u for u in USERS}
USERNAME_MAPPING = {u.username: u for u in USERS}


def authenticate(username, password):
    """Returns user object if exists, otherwise return None.
    :param username: string.
    :param password: string.
    :return: dictionary {'id': <id>, 'username': <username>, 'password': <password>}.
    """
    user = USERNAME_MAPPING.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    """Returns user id if exists, otherwise returns None.
    :param payload: dictionary.
    :return: user id.
    """
    user_id = payload['identity']
    return USERID_MAPPING.get(user_id, None)
