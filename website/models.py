from datetime import datetime
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Livre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10000))
    date_created = db.Column(db.String(14))
    price = db.Column(db.Integer)
    link_image = db.Column(db.String(10000))

    def __init__(self, title, date_created, price, link_image):
        self.title = title
        self.date_created = date_created
        self.price = price
        self.link_image = link_image


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    def __init__(self, email, password, first_name):
        self.email = email
        self.password = password
        self.first_name = first_name



