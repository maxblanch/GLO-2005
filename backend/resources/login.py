from flask_restful import Resource, request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    jwt_optional,
    fresh_jwt_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)
import hashlib
from models.Coworker import CoworkerModel, CoworkerSchema
from models.Manager import ManagerModel, ManagerSchema

class UserLogin(Resource):
    @classmethod
    def post(cls):
        coworker_schema = CoworkerSchema(strict=True)
        manager_schema = ManagerSchema(strict=True)
        user_data = coworker_schema.load(request.get_json()).data
        user = CoworkerModel.find_by_username(user_data['username'])
        
        if user and safe_str_cmp(user.password, hashlib.md5(user_data['password'].encode("utf")).hexdigest()):
            access_token = create_access_token(identity='coworker '+str(user.coworker_id), fresh=True)
            refresh_token = create_refresh_token(user.coworker_id)
            return {"access_token": access_token, "refresh_token": refresh_token, "type": "coworker"}, 200
        
        if not user: 
            user_data = manager_schema.load(request.get_json()).data
            user = ManagerModel.find_by_username(user_data['username'])
            
        if user and safe_str_cmp(user.password, hashlib.md5(user_data['password'].encode("utf")).hexdigest()):
            access_token = create_access_token(identity='manager '+str(user.manager_id), fresh=True)
            refresh_token = create_refresh_token(user.manager_id)
            return {"access_token": access_token, "refresh_token": refresh_token, "type": "manager"}, 200
            

        return {"message": "Invalid credentials!"}, 401

