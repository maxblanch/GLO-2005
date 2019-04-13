from db import db, ma
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
        db.engine.execute("INSERT INTO `Coworker` (first_name, last_name, email, gender, username, password, address, postal_area, city, state, country) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (self.first_name, self.last_name, self.email, self.gender, self.username, self.password, self.address, self.postal_area, self.city, self.state, self.country))

    @classmethod
    def delete_from_db(cls, coworker_id):
        db.engine.execute("DELETE FROM Coworker WHERE coworker_id=%s", (coworker_id))

    @classmethod
    def get_all(cls):
        return db.engine.execute("SELECT * FROM Coworker")

    @classmethod
    def find_by_id(cls, id):
        return db.engine.execute("SELECT * FROM Coworker WHERE coworker_id=%s", (id)).fetchone()

    @staticmethod
    def hashPassword(password):
        return hashlib.md5(password.encode("utf")).hexdigest()
    
    @classmethod
    def find_by_username(cls, username):
        return db.engine.execute("SELECT * FROM Coworker WHERE username=%s", (username)).fetchone()

    @classmethod
    def find_by_email(cls, email):
        return db.engine.execute("SELECT * FROM Coworker WHERE email=%s", (email)).fetchone()


class CoworkerSchema(ma.Schema):
    class Meta:
        fields = ('coworker_id', 'username', 'first_name', 'last_name', 'email', 
                    'gender', 'username', 'password', 'address', 'postal_area', 'city', 'state', 'country')
        load_only = ('password',)