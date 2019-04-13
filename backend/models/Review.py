from db import db, ma

class ReviewModel(db.Model):
    __tablename__ = 'Review'

    review_id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(45), nullable=False)
    comment = db.Column(db.String(2000), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    date = db.Column(db.DateTime())
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
        db.engine.execute("INSERT INTO `Review` (title, comment, rating, cws_id, coworker_id) VALUES (%s,%s,%s,%s,%s)",
                           (self.title, self.comment, self.rating, self.cws_id, self.coworker_id))
        db.session.commit()

    @classmethod
    def find_by_cws_id_and_coworker_id(cls, cws_id, coworker_id):
        return cls.query.filter_by(cws_id=cws_id, coworker_id=coworker_id).first()

    @classmethod
    def find_by_id(cls, review_id):
        return cls.query.filter_by(review_id=review_id).first()
        

    @classmethod
    def find_by_cwspace(cls, cws_id):
        return cls.query.filter_by(cws_id=cws_id).all()


class ReviewSchema(ma.Schema):
    class Meta:
        fields = ('review_id', 'title', 'comment', 'rating', 'cws_id', 'coworker_id', 'date')