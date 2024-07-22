from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from .database import db


class Product(db.Model):
    name: Mapped[str] = mapped_column(String(100), unique=True)
    price: Mapped[int]
