from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.Coworker import CoworkerModel, CoworkerSchema

coworker_schema = CoworkerSchema(strict=True)
coworkers_schema = CoworkerSchema(many=True, strict=True)

class Coworkers(Resource):
    def get(self):
        coworkers = CoworkerModel.get_all()
        data = coworkers_schema.dump(coworkers).data
        if (data):
            return jsonify(data)
        else:
            return {'message': 'No Coworkers Found'}, 404


class Coworker(Resource):
    def get(self, id):
        cw = CoworkerModel.find_by_id(id)
        data = coworker_schema.dump(cw).data
        if data: return jsonify(data)
        return {'message': 'Coworker not found'}, 404


class CoworkerDelete(Resource):
    @jwt_required
    def delete(cls):
        token_data = get_jwt_identity().split()
        if (token_data[0] == 'coworker'):
            user = CoworkerModel.find_by_id(token_data[1])
            if not user:
                return {"message": "User not found."}, 404

            CoworkerModel.delete_from_db(user.coworker_id)
            return {"message": "User deleted"}, 200
        else:
            return {"message": "Authorization needed"}, 401


class CoworkerRegister(Resource):
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
        data = CoworkerRegister.parser.parse_args()

        if CoworkerModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        if CoworkerModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400

        user = CoworkerModel(data['first_name'], data['last_name'], data['email'], data['gender'], data['username'], data['password'], 
                             data['address'], data['postal_area'], data['city'], data['state'], data['country'])
        user.save_to_db()
        user = coworker_schema.dump(user).data

        return {"message": "User created successfully.",
                "user_info": user}, 201
