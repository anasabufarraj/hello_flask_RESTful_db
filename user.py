#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
"""User credentials module."""

import sqlite3


class User:
    """User object."""
    def __init__(self, _id, _username, _password):
        self.id = _id
        self.username = _username
        self.password = _password

    @classmethod
    def find_user_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        result = cursor.execute('SELECT * FROM users WHERE username=?',
                                (username, ))
        row = result.fetchone()
        if row:
            user = cls(*row)  # cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_user_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        result = cursor.execute('SELECT * FROM users WHERE id=?', (_id, ))
        row = result.fetchone()
        if row:
            user = cls(*row)  # cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user
