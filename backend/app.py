from mysql.connector import MySQLConnection, Error
from flask import Flask, request, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from security import user_login

# Imports of RESTful Api routes Ressources
from resources.coworker import Coworkers, Coworker, CoworkerRegister
from resources.manager import Managers, Manager, ManagerRegister
from resources.cwspace import Cwspaces, Cwspace, CwspacesSearch
from resources.review import Reviews, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:glo2005@localhost:3306/WeShare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'glo2005'
api = Api(app)

jwt = JWTManager(app)
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user =  user_login(username, password)
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    if (user[0] == 'coworker'): return jsonify(coworker_id=user[1].coworker_id ,access_token=access_token), 200
    if (user[0] == 'manager'): return jsonify(manager_id=user[1].manager_id ,access_token=access_token), 200


api.add_resource(Coworkers, '/coworkers')
api.add_resource(Coworker, '/coworker/<int:id>')
api.add_resource(CoworkerRegister, '/coworker/register')

api.add_resource(Managers, '/managers')
api.add_resource(Manager, '/manager/<int:id>')
api.add_resource(ManagerRegister, '/manager/register')

api.add_resource(Cwspaces, '/cwspaces')
api.add_resource(CwspacesSearch, '/cwspaces/<string:query>')
api.add_resource(Cwspace, '/cwspace/<int:id>')

api.add_resource(Reviews, '/reviews')
api.add_resource(Review, '/review/<int:cws_id>_<int:coworker_id>')

if __name__ == '__main__':
    from db import db, ma
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True, port=5000)
