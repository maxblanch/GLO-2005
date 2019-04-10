from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, request
from models.CoworkingSpaces import CoworkingSpacesModel, CoworkingSpaceSchema

class Cwspaces(Resource):
    def get(self):
        cwspaces_schema = CoworkingSpaceSchema(many=True, strict=True)
        results = CoworkingSpacesModel.query.all()
        results = cwspaces_schema.dump(results)
        return jsonify(results.data)
        # return {'data': list(map(lambda x: x.json(), CoworkingSpacesModel.query.all()))}

    @jwt_required
    def post(self):
        cwspace_schema = CoworkingSpaceSchema(strict=True)
        data = cwspace_schema.load(request.get_json()).data
        cwspace = CoworkingSpacesModel(data['name'],
        data['address'], data['image_url'], data['currency'], data['day_price'],
        data['description'], data['postal_area'], data['city'], data['state'], 
        data['country'], data['week_price'], data['month_price'], data['manager_id'])

        cwspace.save_to_db()
        return {"message": f"Coworking Space created successfully.",
                "cws_id": cwspace.cws_id}, 201

        

class CwspacesSearch(Resource):
    def get(self, query):
        query = query.split()[0]
        if (len(query) >= 3):
            cwspaces_schema = CoworkingSpaceSchema(many=True, strict=True)
            results = CoworkingSpacesModel.find_by_name_city_state_country(query)
            results = cwspaces_schema.dump(results)
            return jsonify(results.data)
        # return {'data': list(map(lambda x: x.json(), CoworkingSpacesModel.find_by_country(query)))}


class Cwspace(Resource):
    def get(self, id):
        cw = CoworkingSpacesModel.find_by_id(id)
        if cw: return cw.json()
        return {'message': 'Coworker not found'}, 404