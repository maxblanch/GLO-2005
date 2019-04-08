from db import db

class CoworkingSpacesModel(db.Model): 
    __tablename__ = 'CoworkingSpace'

    cws_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45), nullable=False)
    image_url = db.Column(db.String(2083), unique=True)
    currency = db.Column(db.String(3), nullable=False)
    day_price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    rating = db.Column(db.Float())
    postal_area = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    country = db.Column(db.String(45), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    week_price = db.Column(db.Integer(), nullable=False)
    month_price = db.Column(db.Integer(), nullable=False)
    manager_id = db.Column(db.Integer(), db.ForeignKey('Manager.manager_id'))

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(cws_id=id).first()

    def json(self):
        return {
            'name': self.name,
            'address': self.address,
            'country': self.country,
        }

