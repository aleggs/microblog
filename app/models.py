from app import db

class User(db.Model): # db.Model is basically a SQLAlchemy Class
    # what I'm doing here is building a python class that is also a db class
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
