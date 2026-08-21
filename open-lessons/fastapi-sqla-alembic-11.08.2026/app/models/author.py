from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.book import Book


class Author(TimestampMixin, Base):
    __table_args__ = (
        CheckConstraint(
            "length(name) <= 120",
            name="ck_author_name_length",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text, unique=True)
    email: Mapped[str | None] = mapped_column(Text, unique=True)
    books: Mapped[list[Book]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
        passive_deletes=True,
        order_by="Book.id",
        lazy="raise",
    )
