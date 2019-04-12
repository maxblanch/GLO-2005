from db import db, ma
from sqlalchemy import or_

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
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    week_price = db.Column(db.Integer(), nullable=False)
    month_price = db.Column(db.Integer(), nullable=False)
    manager_id = db.Column(db.Integer(), db.ForeignKey('Manager.manager_id'))

    def __init__(self, name, address, image_url, currency, day_price, description, postal_area, city, state, country, week_price, month_price, manager_id):
        self.name = name
        self.address = address
        self.image_url = image_url
        self.currency = currency
        self.day_price = day_price
        self.description = description
        self.postal_area = postal_area
        self.city = city
        self.state = state
        self.country = country
        self.week_price = week_price
        self.month_price = month_price
        self.manager_id = manager_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def get_all(cls):
        return db.engine.execute("SELECT * FROM CoworkingSpace")

    @classmethod
    def find_by_id(cls, id):
        data = db.engine.execute("SELECT * FROM CoworkingSpace WHERE cws_id = %s", (id))
        result = data.fetchone()
        data.close()
        return result

    @classmethod
    def find_by_cities(cls, city):
        data = db.engine.execute("SELECT * FROM CoworkingSpace WHERE city LIKE %s", (f"%{city}%"))
        result = data.fetchall()
        data.close()
        return result

    @classmethod
    def find_by_name_city_state_country(cls, query):
        return cls.query.filter(or_(cls.country.ilike(f"%{query}%"),
                                    cls.name.ilike(f"%{query}%"),
                                    cls.city.ilike(f"%{query}%"),
                                    cls.state.ilike(f"%{query}%"))).all()


class CoworkingSpaceSchema(ma.Schema):
    class Meta:
        fields = ('cws_id', 'name', 'address', 'image_url', 'currency', 'day_price', 'description', 'rating', 'postal_area', 'city', 'state', 'country', 'week_price', 'month_price', 'manager_id')