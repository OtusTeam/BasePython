from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Text

from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(
        String,
        nullable=False,
        unique=True,
        default="",
        server_default="",
    )
    description = Column(Text, nullable=False, default="", server_default="")

    if TYPE_CHECKING:
        query: Query
