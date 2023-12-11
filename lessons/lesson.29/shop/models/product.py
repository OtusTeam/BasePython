from sqlalchemy import Column, String
from .database import db


class Product(db.Model):
    name = Column(String, nullable=False)
