from datetime import date

from .database import db


class Person(db.Model):
    class Meta:
        required_fields = {
            "verbose_name": ["name", "birth_date"],
        }

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    computers = db.relationship("Computer", back_populates="person")
    email = db.Column(db.String)

    @property
    def verbose_name(self):
        timedelta = date.today() - self.birth_date
        return f"{self.name} ({int(timedelta.days // 365.25)} y.o.)"
