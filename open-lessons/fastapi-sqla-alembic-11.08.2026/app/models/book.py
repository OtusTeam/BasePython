from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.author import Author


class Book(TimestampMixin, Base):
    __table_args__ = (
        CheckConstraint(
            "length(title) <= 200",
            name="ck_book_title_length",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(
        ForeignKey("author.id", ondelete="CASCADE"),
        index=True,
    )
    author: Mapped[Author] = relationship(back_populates="books")
