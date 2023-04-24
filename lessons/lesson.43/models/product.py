from typing import TYPE_CHECKING, Type

from sqlalchemy import Column, String, Integer

from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    short_description = Column(
        String(200),
        nullable=False,
        default="",
        server_default="",
    )

    # if TYPE_CHECKING:
    #     query: Query


if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model

    Product: Type[Model]
