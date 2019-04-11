from flask import jsonify
from flask_restful import Resource, reqparse, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.Review import ReviewModel, ReviewSchema

reviews_schema = ReviewSchema(many=True, strict=True)
review_schema = ReviewSchema(strict=True)

class Reviews(Resource):
    def get(self):
        reviews = ReviewModel.query.all()
        data = reviews_schema.dump(reviews).data
        if (data):
            return jsonify(data)
        else:
            return {'message': 'No Reviews Found'}, 404

    @jwt_required
    def post(self):
        token_data = get_jwt_identity().split()
        if (token_data[0] != 'coworker'): return {'message': 'Reviews can only be done by coworkers'}, 401
        review_data = review_schema.load(request.get_json()).data
        review = ReviewModel(review_data['title'], review_data['comment'],
        review_data['rating'], review_data['cws_id'], token_data[1])
        try:
            review.save_to_db()
        except:
            return {"message": "User already did a review for this coworking space"}, 400
        return {"message": f"Review created successfully.",
                "cws_id": review.cws_id,
                "coworker_id": review.coworker_id}, 201


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
    def get(self, review_id):
        cw = ReviewModel.find_by_id(review_id)
        data = review_schema.dump(cw).data
        if data: return jsonify(data)
        return {'message': 'Review Not Found'}, 404
