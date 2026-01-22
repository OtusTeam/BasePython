from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import CreatedAtMixin
from models.post_tag_association import post_tag_association_table

if TYPE_CHECKING:
    from models.post import Post


class Tag(CreatedAtMixin, Base):
    # CITEXT вместо Text
    name: Mapped[str] = mapped_column(Text, primary_key=True)

    posts: Mapped[list["Post"]] = relationship(
        secondary=post_tag_association_table,
        back_populates="tags",
    )

    # id: int pk
    # name: text, unique constraint on func.lower(name)
    # или
    # name: CITEXT, unique

    __table_args__ = (
        CheckConstraint(
            func.length(name) <= 100,
            "name_length",
        ),
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"

    def __repr__(self) -> str:
        return str(self)
