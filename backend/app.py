from flask import Flask, request, jsonify
from mysql.connector import MySQLConnection, Error
from controllers.coworking_space import CoworkingSpace
from controllers.coworker import Coworker
from controllers.manager import Manager
from controllers.review import Review

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Docker!!!!"

# Coworking spaces Routes
@app.route('/cwspaces', methods=['GET'])
def get_cwspaces():
    return CoworkingSpace().get_cwspaces()

@app.route('/cwspaces/<id>', methods=['GET'])
def get_cwspace(id):
    return CoworkingSpace().get_cwspace(id)


# Coworkers Routes
@app.route('/coworkers', methods=['GET'])
def get_coworkers():
    return Coworker().get_coworkers()

@app.route('/coworkers/<id>', methods=['GET'])
def get_coworker(id):
    return Coworker().get_coworker(id)


# Manager Routes
@app.route('/managers', methods=['GET'])
def get_managers():
    return Manager().get_managers()

@app.route('/managers/<id>', methods=['GET'])
def get_manager(id):
    return Manager().get_manager(id)


# Reviews Routes
@app.route('/reviews', methods=['GET'])
def get_reviews():
    return Review().get_reviews()

@app.route('/reviews/<cws_id>_<coworker_id>')
def get_review(cws_id, coworker_id):
    return Review().get_review(cws_id, coworker_id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
