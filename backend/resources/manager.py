from flask_restful import Resource, reqparse
from models.Manager import ManagerModel

class Managers(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ManagerModel.query.all()))}


class Manager(Resource):
    def get(self, id):
        cw = ManagerModel.find_by_id(id)
        if cw: return cw.json()
        return {'message': 'Coworker not found'}, 404


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

        user = ManagerModel(data['first_name'], data['last_name'], data['email'], data['gender'], data['username'], data['password'], 
                             data['address'], data['postal_area'], data['city'], data['state'], data['country'])
        user.save_to_db()

        return {"message": "Manager created successfully."}, 201