from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from models.database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, default="", server_default="")
    is_new = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
