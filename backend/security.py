import hashlib
from werkzeug.security import safe_str_cmp
from models.Coworker import CoworkerModel


def authenticate(username, password):
    user = CoworkerModel.find_by_username(username)
    if user and safe_str_cmp(user.password, hashlib.md5(password.encode("utf")).hexdigest()):
        return user


def identity(payload):
    user_id = payload['identity']
    return CoworkerModel.find_by_id(user_id)