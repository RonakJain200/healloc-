from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    specialization = db.Column(db.String(150))
    experience = db.Column(db.Integer)
    location = db.Column(db.String(150))
    pincode = db.Column(db.String(10))
    degree = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
