from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base

if TYPE_CHECKING:
    from . import Publication


class Author(Base):

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(250),
        nullable=True,
        unique=True,
    )
    bio: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )
    ref_code: Mapped[str] = mapped_column(
        unique=True,
    )

    publications: Mapped[list["Publication"]] = relationship(
        back_populates="author",
    )

    # def get_top_publications(self) -> list[Publication]:
    #     stmt = (
    #         select(Publication)
    #         .where(Publication.author_id == self.id)
    #         .order_by(Publication.citation_count.desc())
    #     )

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f" name={self.name!r}"
            f" email={self.email!r}"
            f")"
        )
