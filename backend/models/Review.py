from db import db
import hashlib

class ReviewModel(db.Model):
    __tablename__ = 'Review'

    title = db.Column(db.String(45), nullable=False)
    comment = db.Column(db.String(2000), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    cws_id = db.Column(db.Integer(), db.ForeignKey('CoworkingSpace.cws_id'), primary_key=True)
    coworker_id = db.Column(db.Integer(), db.ForeignKey('Coworker.coworker_id'), primary_key=True)

    def __init__(self, title, 
                       comment, 
                       rating, 
                       cws_id, 
                       coworker_id):
        self.title = title
        self.comment = comment
        self.rating = rating
        self.cws_id = cws_id
        self.coworker_id = coworker_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, cws_id, coworker_id):
        return cls.query.filter_by(cws_id=cws_id, coworker_id=coworker_id).first()

    
    def json(self):
        return {
            'title': self.title,
            'comment': self.comment,
            'rating': self.rating,
            'cws_id': self.cws_id,
            'coworker_id': self.coworker_id
        }