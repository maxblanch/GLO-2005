from flask import Flask, request, jsonify
from flask_restful import Api
from flask_jwt import JWT
from mysql.connector import MySQLConnection, Error
from resources.coworker import Coworkers, Coworker, CoworkerRegister
from resources.manager import Managers, Manager, ManagerRegister
from resources.cwspace import Cwspaces, Cwspace
from resources.review import Reviews, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:glo2005@localhost:3306/WeShare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


api.add_resource(Coworkers, '/coworkers')
api.add_resource(Coworker, '/coworker/<int:id>')
api.add_resource(CoworkerRegister, '/coworker/register')

api.add_resource(Managers, '/managers')
api.add_resource(Manager, '/manager/<int:id>')
api.add_resource(ManagerRegister, '/manager/register')

api.add_resource(Cwspaces, '/cwspaces')
api.add_resource(Cwspace, '/cwspace/<int:id>')

api.add_resource(Reviews, '/reviews')
api.add_resource(Review, '/review/<int:cws_id>_<int:coworker_id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, port=5000)
