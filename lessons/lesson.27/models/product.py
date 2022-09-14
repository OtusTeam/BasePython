from sqlalchemy import Column, Integer, String, Boolean
from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    is_new = Column(Boolean, nullable=False, default=False, server_default="FALSE")
