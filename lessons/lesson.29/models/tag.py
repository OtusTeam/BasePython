from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey, CheckConstraint, func

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.post_tag import post_tag_association_table
from models.mixins import IdIntPk

if TYPE_CHECKING:
    from models.post import Post


class Tag(IdIntPk, Base):

    slug: Mapped[str] = mapped_column(
        Text,  # todo: CITEXT: 1. enable citext extension; 2. set CITEXT type for PG
        unique=True,
    )
    display_name: Mapped[str] = mapped_column(
        Text,
        unique=True,
    )
    posts: Mapped[list["Post"]] = relationship(
        secondary=post_tag_association_table,
        back_populates="tags",
    )

    __table_args__ = (
        CheckConstraint(
            func.length(slug) <= 32,
            name="slug_length",
        ),
        CheckConstraint(
            func.length(display_name) <= 64,
            name="display_name_length",
        ),
    )

    def __str__(self) -> str:
        return f"{self.display_name} ({self.slug})"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, slug={self.slug!r}, display_name={self.display_name!r})"
