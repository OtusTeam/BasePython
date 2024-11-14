from sqlalchemy.orm import Mapped, mapped_column

from .flask_db import db
from .int_id_pk_mixin import IntIdPkMixin


class Product(IntIdPkMixin, db.Model):
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int]

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name!r}, "
            f"price={self.price}"
            f")"
        )

    def __repr__(self):
        return str(self)
