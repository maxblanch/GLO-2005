from flask import jsonify
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


class ReviewsForCWspace(Resource):
    def get(self, cws_id):
        reviews_schema = ReviewSchema(many=True, strict=True)
        reviews = ReviewModel.find_by_cwspace(cws_id)

        if (reviews):
            reviews = reviews_schema.dump(reviews)
            return jsonify(reviews.data)
        else:
            return {'message': 'No reviews for the specified Coworking Space'}, 404


class Review(Resource):
    def get(self, cws_id, coworker_id):
        cw = ReviewModel.find_by_id(cws_id, coworker_id)
        if cw: return cw.json()
        return {'message': 'Review Not Found'}, 404
