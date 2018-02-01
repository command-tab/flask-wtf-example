from app.models import db


class Category(db.Model):

    id = db.Column(db.Integer(), db.Sequence('category_id_seq'), autoincrement=True, primary_key=True)
    name = db.Column(db.Unicode(), nullable=False)

    def __init__(self, name):
        self.name = name
