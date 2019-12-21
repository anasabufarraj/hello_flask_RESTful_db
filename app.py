#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj.
# ------------------------------------------------------------------------------
"""Learning how to build Flask REST API with database extension."""

from datetime import timedelta

from flask import Flask, jsonify, render_template, request, current_app
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, Api, reqparse

from security import authenticate, identity

APP = Flask(__name__)

APP.secret_key = 'D195A7937E1C15FF1925A72593EBE812160CFB909CAE23D3E4B46EBD7AA81D53'
APP.config['JWT_AUTH_URL_RULE'] = '/login'
APP.config['JWT_AUTH_USERNAME_KEY'] = 'username'
APP.config['JWT_AUTH_PASSWORD_KEY'] = 'password'
APP.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

API = Api(APP)
JWT = JWT(APP, authenticate, identity)

# ------------------------------------------------------------------------------
# Database Setup:
# ------------------------------------------------------------------------------
ITEMS = [{'name': 'book', 'price': 17.99}]  # TODO: Store in database isntead


# ------------------------------------------------------------------------------
# Application Error Handlers:
# ------------------------------------------------------------------------------
@JWT.auth_response_handler
def response_handler(access_token, user):
    """Returns access token and stored user id."""
    return jsonify({
        'access_token': access_token.decode('utf-8'),
        'user_id': user.id,
        'username': user.username
    })


@JWT.jwt_error_handler
def error_handler(error):
    """Returns JSON object with response code and message with response
    code in the header."""
    return jsonify({
        'code': error.status_code,
        'message': error.description,
    }), error.status_code


# ------------------------------------------------------------------------------
# Application Routes:
# ------------------------------------------------------------------------------
@APP.route('/')
def index():
    """Returns home page template with details."""
    user_agent = request.user_agent
    app_name = current_app.name
    return render_template('index.html', user_agent=user_agent, app_name=app_name), 200


# ------------------------------------------------------------------------------
# Application Classes:
# ------------------------------------------------------------------------------
class ItemList(Resource):
    """Dealing with store item listing."""
    @jwt_required()
    def get(self):
        """Returns a JSON of all items with 200 (OK) response."""
        return {'items': ITEMS}, 200


class Item(Resource):
    """Manage store items."""
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be blank!')

    @jwt_required()
    def get(self, name):
        """Returns item by name if found.
        Lazy iterate over a filter object with next, return an item if found, or return None.
        :param name: string.
        :returns: {"item": <name>} or {"item": null}, 200 (OK) if True, otherwise 404 (NOT FOUND).
        """
        item = next(filter(lambda x: x['name'] == name, ITEMS), None)
        return item, 200 if item else 404

    @jwt_required()
    def post(self, name):
        """Creates and append new item, if exists returns a message and 400 (BAD REQUEST).
        :param name: string.
        :returns: item and 201 (CREATED).
        """
        item = next(filter(lambda x: x['name'] == name, ITEMS), None)
        if item:
            return {'message': f'item with name {name} already exists!'}, 400

        request_data = Item.parser.parse_args()
        item = {'name': name, 'price': request_data['price']}
        ITEMS.append(item)

        return item, 201

    @jwt_required()
    def delete(self, name):
        """Deletes item if exist and return message, otherwise returns message and 400 (BAD REQUEST).
        Deletion happens by overwriting existing items database, and returns new
        constructed database excluding named item.
        :param name: string.
        :return: new constructed items database and 200 (OK), otherwise message and
        400 (BAD REQUEST).
        """
        global ITEMS
        item = next(filter(lambda x: x['name'] == name, ITEMS), None)
        if item:
            ITEMS = [next(filter(lambda x: x['name'] != name, ITEMS), None)]
            print(ITEMS)
            return {'message': 'item deleted'}, 200
        return {'message': 'item not exists'}, 400

    @jwt_required()
    def put(self, name):
        """Returns updated item if exists and 200 (OK), otherwise add item to database.
        :param name: string.
        :return: item as dictionary
        """
        request_data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, ITEMS), None)
        if item:
            item.update(request_data)
        else:
            item = {'name': name, 'price': request_data['price']}
            ITEMS.append(item)
        return item, 200


# ------------------------------------------------------------------------------
# API Resources:
# ------------------------------------------------------------------------------
API.add_resource(ItemList, '/item')
API.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    APP.run()
