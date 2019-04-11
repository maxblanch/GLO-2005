from db import db, ma
import hashlib

class ReviewModel(db.Model):
    __tablename__ = 'Review'

    title = db.Column(db.String(45), nullable=False)
    comment = db.Column(db.String(2000), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    # date = db.Column(db.DateTime(), nullable=False)
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
        # db.session.add(self)
        db.engine.execute("INSERT INTO `Review` (title, comment, rating, cws_id, coworker_id) VALUES (%s,%s,%s,%s,%s)",
                           (self.title, self.comment, self.rating, self.cws_id, self.coworker_id))
        db.session.commit()

    @classmethod
    def find_by_id(cls, cws_id, coworker_id):
        return cls.query.filter_by(cws_id=cws_id, coworker_id=coworker_id).first()

    @classmethod
    def find_by_cwspace(cls, cws_id):
        return cls.query.filter_by(cws_id=cws_id).all()


class ReviewSchema(ma.Schema):
    class Meta:
        fields = ('title', 'comment', 'rating', 'cws_id', 'coworker_id', 'date')