__all__ = (
    "Base",
    "db",
)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)


db = SQLAlchemy(model_class=Base)
