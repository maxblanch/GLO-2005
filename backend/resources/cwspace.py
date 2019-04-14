from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request
from models.CoworkingSpaces import CoworkingSpacesModel, CoworkingSpaceSchema

coworkingSpace_schema = CoworkingSpaceSchema(strict=True)

class Cwspaces(Resource):
    def get(self):
        data = CoworkingSpacesModel.get_all()
        cwspaces_schema = CoworkingSpaceSchema(many=True, strict=True)
        results = cwspaces_schema.dump(data)
        return jsonify(results.data)


class CwspaceByCities(Resource):
    def get(self, city):
        cwspaces_schema = CoworkingSpaceSchema(many=True, strict=True)
        data = CoworkingSpacesModel.find_by_cities(city)
        if (data):
            data = cwspaces_schema.dump(data)
            return jsonify(data.data)
        else:
            return {'message': 'No Coworking spaces found for this city'}, 404


class CwspacesSearch(Resource):
    def get(self, query):
        query = query.split()[0]
        if (len(query) >= 3):
            cwspaces_schema = CoworkingSpaceSchema(many=True, strict=True)
            results = CoworkingSpacesModel.find_by_name_city_state_country(query)
            results = cwspaces_schema.dump(results).data
            if (len(results) != 0): return jsonify(results)
            return {'message': 'No Coworking Spaces Found'}, 404


class Cwspace(Resource):
    def get(self, id):
        cw = CoworkingSpacesModel.find_by_id(id)
        data = coworkingSpace_schema.dump(cw).data
        if data: return jsonify(data)
        return {'message': 'Coworking Space Not Found'}, 404

    @jwt_required
    def delete(self, id):
        cw = CoworkingSpacesModel.find_by_id(id)
        if (cw):
            cw_data = coworkingSpace_schema.dump(cw).data
            token_data = get_jwt_identity().split()
            if (token_data[0] == 'manager' and int(token_data[1]) == cw_data['manager_id']):
                CoworkingSpacesModel.delete_from_db(cw.cws_id)
                return {'message': f"Coworking space id: {cw_data['cws_id']} deleted"}, 200
            else:
                return {'message': 'Unauthorized'}, 401
        else:
            return {'message': 'Coworking Space Not Found'}, 404


class CwspaceAdd(Resource):
    @jwt_required
    def post(self):
        token_data = get_jwt_identity().split()
        cwspace_schema = CoworkingSpaceSchema(strict=True)
        data = cwspace_schema.load(request.get_json()).data

        if ('manager' != token_data[0]): return {'message': 'Authorization Needed'}, 401
            
        cwspace = CoworkingSpacesModel(data['name'],
        data['address'], data['image_url'], data['currency'], data['day_price'],
        data['description'], data['postal_area'], data['city'], data['state'], 
        data['country'], data['week_price'], data['month_price'], token_data[1])

        cwspace.save_to_db()
        last_cws = CoworkingSpacesModel.get_last_id()
        return {"message": f"Coworking Space created successfully.",
                "cws_id": last_cws.cws_id}, 201