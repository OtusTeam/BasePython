from models.database import db


class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    person = db.relationship("Person", back_populates="computers")
