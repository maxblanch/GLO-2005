from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required
from models.Review import ReviewModel, ReviewSchema

class Reviews(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ReviewModel.query.all()))}

    @jwt_required
    def post(self):
        review_schema = ReviewSchema(strict=True)
        review_data = review_schema.load(request.get_json()).data
        
        review = ReviewModel(review_data['title'], review_data['comment'],
        review_data['rating'], review_data['cws_id'], review_data['coworker_id'])

        try:
            review.save_to_db()
            return {"message": f"Review created successfully.",
                    "cws_id": review.cws_id,
                    "coworker_id": review.coworker_id}, 201
        except:
            return {"message": "User already did a review for this coworking space"}, 401


class Review(Resource):
    def get(self, cws_id, coworker_id):
        cw = ReviewModel.find_by_id(cws_id, coworker_id)
        if cw: return cw.json()
        return {'message': 'Review Not Found'}, 404
