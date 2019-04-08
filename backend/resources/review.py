from flask_restful import Resource, reqparse
from models.Review import ReviewModel

class Reviews(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ReviewModel.query.all()))}


class Review(Resource):
    def get(self, cws_id, coworker_id):
        cw = ReviewModel.find_by_id(cws_id, coworker_id)
        if cw: return cw.json()
        return {'message': 'Review Not Found'}, 404
