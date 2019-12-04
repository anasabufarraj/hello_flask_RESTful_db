#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""User credentials module."""


class User:
    """User object."""
    def __init__(self, _id, _username, _password):
        self.id = _id
        self.username = _username
        self.password = _password
