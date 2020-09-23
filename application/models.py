from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))

    def __init__(self, password, email, firstName, lastName):
        self.password = password
        self.email = email
        self.first_name = firstName
        self.last_name = lastName