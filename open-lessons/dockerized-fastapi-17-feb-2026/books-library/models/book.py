from uuid import UUID
from datetime import date

from sqlalchemy import func, Text
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[UUID] = mapped_column(
        server_default=func.uuidv7(),
        primary_key=True,
    )
    title: Mapped[str] = mapped_column(
        Text,
        index=True,
        default="",
        server_default="",
    )
    pub_date: Mapped[date] = mapped_column()
