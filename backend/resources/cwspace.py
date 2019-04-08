from flask_restful import Resource
from models.CoworkingSpaces import CoworkingSpacesModel

class Cwspaces(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), CoworkingSpacesModel.query.all()))}


class Cwspace(Resource):
    def get(self, id):
        cw = CoworkingSpacesModel.find_by_id(id)
        if cw: return cw.json()
        return {'message': 'Coworker not found'}, 404