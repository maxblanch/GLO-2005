from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.Coworker import CoworkerModel, CoworkerSchema

coworker_schema = CoworkerSchema(strict=True)

class Coworkers(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), CoworkerModel.query.all()))}


class Coworker(Resource):
    def get(self, id):
        cw = CoworkerModel.find_by_id(id)
        data = coworker_schema.dump(cw).data
        if data: return jsonify(data)
        return {'message': 'Coworker not found'}, 404

    @jwt_required
    def delete(cls, id: int):
        user = CoworkerModel.find_by_id(id)
        if not user:
            return {"message": "User not found."}, 404
        
        user.delete_from_db()
        return {"message": "User deleted"}, 200


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

        user = CoworkerModel(data['first_name'], data['last_name'], data['email'], data['gender'], data['username'], data['password'], 
                             data['address'], data['postal_area'], data['city'], data['state'], data['country'])
        user.save_to_db()
        user = coworker_schema.dump(user).data

        return {"message": "User created successfully.",
                "user_info": user}, 201
