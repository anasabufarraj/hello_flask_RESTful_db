#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj.
# ------------------------------------------------------------------------------

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS users (id INT, username TEXT, password TEXT)')

connection.commit()
connection.close()
