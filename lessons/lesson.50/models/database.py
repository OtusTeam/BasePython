__all__ = (
    "db",
)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


db = SQLAlchemy(model_class=Base)
