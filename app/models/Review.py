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

    @classmethod
    def get_all(cls):
        return db.engine.execute("SELECT * FROM Review").fetchall()

    @classmethod
    def find_by_id(cls, review_id):
        return db.engine.execute("SELECT * FROM Review WHERE review_id=%s", (review_id)).fetchone()
        
    @classmethod
    def find_by_cwsId_coworkerId(cls, cws_id, coworker_id):
        return db.engine.execute("SELECT * FROM Review WHERE cws_id=%s AND coworker_id=%s", (cws_id, coworker_id)).fetchone()

    @classmethod
    def find_by_cwspace(cls, cws_id):
        return db.engine.execute("SELECT * FROM Review WHERE cws_id=%s", (cws_id)).fetchall()


class ReviewSchema(ma.Schema):
    class Meta:
        fields = ('review_id', 'title', 'comment', 'rating', 'cws_id', 'coworker_id', 'date')