from .database import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    computers = db.relationship("Computer", back_populates="person")
