from flask import jsonify
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.Answer import AnswerModel, AnswerSchema

answers_schema = AnswerSchema(many=True, strict=True)
answer_schema = AnswerSchema(strict=True)

class Answers(Resource):
    def get(self):
        answers = AnswerModel.query.all()
        data = answers_schema.dump(answers)
        if (data):
            return jsonify(data)
        else:
            return {'message': 'No Answers Found'}, 404


class Answer(Resource):
    def get(self, review_id):
        answer = AnswerModel.find_by_id(review_id)
        data = answer_schema.dump(answer).data
        if data: return jsonify(data)
        return {'message': 'Answer Not Found'}, 404


class AnswerPost(Resource):
    @jwt_required
    def post(self):
        token_data = get_jwt_identity().split()
        if (token_data[0] != 'manager'): return {'message': 'Answers can only be done by managers'}, 401
        
        body = answer_schema.load(request.get_json()).data
        answer = AnswerModel.find_by_id(body['review_id'])
        if (answer.manager_id != token_data[1]): return {'message': 'Manager can only answer reviews for their Coworking Space'}, 401

        answer = AnswerModel(body['review_id'], body['comment'], token_data[1])

        try:
            answer.save_to_db()
        except:
            return {"message": "Answer already did for this review"}, 400
        
        return {"message": f"Answer created successfully.",
                "review_id": body['review_id']}, 200