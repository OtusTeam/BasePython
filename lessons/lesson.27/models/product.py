from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, default="", server_default="")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    is_new = Column(Boolean, nullable=False, default=False, server_default="FALSE")
