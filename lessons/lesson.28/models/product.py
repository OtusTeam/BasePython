from sqlalchemy.orm import Mapped, mapped_column

from .database import db


class Product(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int | None]
