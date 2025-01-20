from typing import TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin

if TYPE_CHECKING:
    from .author import Author


class Publication(CreatedAtMixin, Base):
    title: Mapped[str]
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    author_id: Mapped[int] = mapped_column(
        ForeignKey("author.id"),
        # ForeignKey(Author.id),
        nullable=False,
    )

    author: Mapped["Author"] = relationship(
        back_populates="publications",
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f" title={self.title!r}"
            f" author_id={self.author_id!r}"
            f")"
        )
