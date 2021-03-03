import json
import os
import configparser

from flask import Flask, request, Response
from pymongo import MongoClient, errors

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')

client = MongoClient(config[os.getenv('ENV')]['db'], 27017)
db = client.db
users =  db.users

def success_response(message):
    return Response(json.dumps(message), status=200, mimetype='application/json')

def error_response(message):
    return Response(message, status=404, mimetype='application/json')

@app.route("/users/<int:userid>", methods=["POST"])
def update_user(userid):
    request_params = request.form
    if 'email' and 'name' not in request_params:
        error_response('Email and name not present in parameters!')
    try:
        db.users.insert_one({
            '_id': userid,
            'email': request_params['email'],
            'name': request_params['name']
        })
    except errors.DuplicateKeyError as e:
        return error_response('Duplicate user id!')
    return success_response(users.find_one({'_id': userid}))


@app.route("/users/<int:userid>", methods=["GET"])
def get_user(userid):
    user = db.users.find_one({'_id': userid})
    if None == user:
        return error_response("No such user found")
    return success_response(user)


@app.route("/users", methods=["GET"])
def get_users():
    request_args = request.args
    limit = int(request_args.get('limit')) if 'limit' in request_args else 10
    offset = int(request_args.get('offset')) if 'offset' in request_args else 0
    user_list = db.users.find().limit(limit).skip(offset)
    if None == users:
        return error_response('No such user found')

    extracted = [
        {
            'userid': d['_id'],
            'name': d['name'],
            'email': d['email']
        } for d in user_list
    ]
    return success_response(extracted)


@app.route("/users/<int:userid>", methods=["DELETE"])
def delete_user(userid):
    db.users.delete_one({'_id': userid})
    return success_response('delete successful', status=200, mimetype='application/json')


def print_hello():
    print('hello')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
