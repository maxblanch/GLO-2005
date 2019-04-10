from mysql.connector import MySQLConnection, Error
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from marshmallow import ValidationError
from db import db, ma

# Imports of RESTful Api routes Ressources
from resources.coworker import Coworkers, Coworker, CoworkerRegister
from resources.manager import Managers, Manager, ManagerRegister
from resources.cwspace import Cwspaces, Cwspace, CwspacesSearch, CwspaceByCities
from resources.review import Reviews, Review, ReviewsForCWspace
from resources.login import UserLogin

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:glo2005@localhost:3306/WeShare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
app.config['JWT_SECRET_KEY'] = 'glo2005'
api = Api(app)

jwt = JWTManager(app)

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

api.add_resource(UserLogin, '/login')

api.add_resource(Coworkers, '/coworkers')
api.add_resource(Coworker, '/coworker/<int:id>')
api.add_resource(CoworkerRegister, '/coworker/register')

api.add_resource(Managers, '/managers')
api.add_resource(Manager, '/manager/<int:id>')
api.add_resource(ManagerRegister, '/manager/register')

api.add_resource(Cwspaces, '/cwspaces')
api.add_resource(CwspaceByCities, '/cwspaces/<string:city>')
api.add_resource(CwspacesSearch, '/cwspaces/<string:query>')
api.add_resource(Cwspace, '/cwspace/<int:id>')

api.add_resource(Reviews, '/reviews')
api.add_resource(ReviewsForCWspace, '/reviews/<int:cws_id>')
api.add_resource(Review, '/review/<int:cws_id>_<int:coworker_id>')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True, port=5000)
