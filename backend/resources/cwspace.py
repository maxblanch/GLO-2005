from flask import jsonify
from flask_restful import Resource, request
from models.CoworkingSpaces import CoworkingSpacesModel, CoworkingSpaceSchema

class Cwspaces(Resource):
    def get(self):
        cwspaces_schema = CoworkingSpaceSchema(many=True, strict=True)
        results = CoworkingSpacesModel.query.all()
        results = cwspaces_schema.dump(results)
        return jsonify(results.data)
        # return {'data': list(map(lambda x: x.json(), CoworkingSpacesModel.query.all()))}

    def post(self):
        cwspace_schema = CoworkingSpaceSchema(strict=True)

        name = request.json['name']
        address = request.json['address']
        image_url = request.json['image_url']
        currency = request.json['currency']
        day_price = request.json['day_price']
        description = request.json['description']
        postal_area = request.json['postal_area']
        city = request.json['city']
        state = request.json['state']
        country = request.json['country']
        week_price = request.json['week_price']
        month_price = request.json['month_price']
        manager_id = request.json['manager_id']

        cwspace = CoworkingSpacesModel(name, address, image_url, currency, day_price, description,
                                        postal_area, city, state, country, week_price, month_price, manager_id)

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