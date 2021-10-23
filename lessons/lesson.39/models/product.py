from datetime import datetime

from sqlalchemy import func

from models.database import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
    )
