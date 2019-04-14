from db import db, ma

class AnswerModel(db.Model):
    __tablename__ = 'Answer'

    review_id = db.Column(db.String(45), db.ForeignKey('Review.review_id'), primary_key=True)
    comment = db.Column(db.String(2000), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    manager_id = db.Column(db.Integer(), db.ForeignKey('Manager.manager_id'))

    def __init__(self, review_id, comment, manager_id):
        self.review_id = review_id
        self.comment = comment
        self.manager_id = manager_id

    def save_to_db(self):
        db.engine.execute("INSERT INTO `Answer` (review_id, comment, manager_id) VALUES (%s,%s,%s)",
                           (self.review_id, self.comment, self.manager_id))
        db.session.commit()

    @classmethod
    def find_by_id(cls, review_id):
        return db.engine.execute("SELECT * FROM Answer WHERE review_id=%s", (review_id)).fetchone()

    @classmethod
    def isManager(cls, manager_id, review_id):
        data = db.engine.execute("SELECT cws_id FROM CoworkingSpace WHERE manager_id=%s AND cws_id IN (SELECT cws_id FROM Review WHERE review_id=%s)", (manager_id, review_id)).fetchone()
        return True if data else False


class AnswerSchema(ma.Schema):
    class Meta:
        fields = ('review_id', 'comment', 'date', 'manager_id')