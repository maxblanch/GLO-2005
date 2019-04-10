from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.Manager import ManagerModel, ManagerSchema

manager_schema = ManagerSchema(strict=True)
managers_schema = ManagerSchema(many=True, strict=True)

class Managers(Resource):
    def get(self):
        data = ManagerModel.query.all()
        data = managers_schema.dump(data).data
        if (data):
            return jsonify(data)
        else:
            return {'message': 'No managers found'}, 404


class Manager(Resource):
    @jwt_required
    def get(self):
        req = get_jwt_identity().split()
        if (req[0] == 'manager'):
            cw = ManagerModel.find_by_id(req[1])
            if cw:
                cw = manager_schema.dump(cw)[0]
                return jsonify(cw)
            else:
                return {'message': 'Manager not found'}, 404
        else:
            return {'message': 'Must be type of Manager'}, 401


class ManagerRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('last_name', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('email', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('gender', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('address', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('postal_area', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('city', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('state', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('country', type=str, required=True, help="This field cannot be blank.")
    
    
    def post(self):
        data = ManagerRegister.parser.parse_args()

        if ManagerModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        if ManagerModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400

        user = ManagerModel(data['first_name'], data['last_name'], data['email'], data['gender'], data['username'], data['password'], 
                             data['address'], data['postal_area'], data['city'], data['state'], data['country'])
        data = manager_schema.dump(user).data
        user.save_to_db()

        return {"message": "Manager created successfully.",
                "data": data}, 201
