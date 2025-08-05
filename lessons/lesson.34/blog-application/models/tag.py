from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import CreatedAtMixin
from models.post_tag_association import PostTagAssociation

if TYPE_CHECKING:
    from models import Post


class Tag(CreatedAtMixin, Base):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(
        String(20),
        unique=True,
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates="tags",
        # secondary=posts_tags_association_table,
        secondary=PostTagAssociation.__table__,
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"
