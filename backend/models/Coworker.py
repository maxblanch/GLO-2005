from db import db
import hashlib

class CoworkerModel(db.Model):
    __tablename__ = 'Coworker'

    coworker_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    gender = db.Column(db.String(45), nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45), nullable=False)
    postal_area = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    country = db.Column(db.String(45), nullable=False)

    def __init__(self, first_name, 
                       last_name, 
                       email, 
                       gender, 
                       username, 
                       password, 
                       address, 
                       postal_area, 
                       city, 
                       state, 
                       country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.username = username
        self.password = self.hashPassword(password)
        self.address = address
        self.postal_area = postal_area
        self.city = city
        self.state = state
        self.country = country

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(coworker_id=id).first()

    @staticmethod
    def hashPassword(password):
        return hashlib.md5(password.encode("utf")).hexdigest()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    def json(self):
        return {
            'id': self.coworker_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'country': self.country,
            'Password': self.password
        }