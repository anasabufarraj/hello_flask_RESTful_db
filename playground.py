#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------

# import sqlite3
#
# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()
#
# cursor.execute(
#     'CREATE TABLE IF NOT EXISTS users (id INT, username TEXT, password TEXT)')
#
# connection.commit()
# connection.close()

from flask import Flask, request

APP = Flask(__name__)

# @APP.route('/')
# def index():
#     foo = request.host_url
#     return f'<p>foo: {foo}</p>'
#
# @APP.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400
#
# if __name__ == '__main__':
#     APP.run(debug=True)
