from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    func,
    CheckConstraint,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    # relationship,
)

from models.base import Base

from models.mixins import CreatedAt
from models.posts_tags_association import PostsTagsAssociation

if TYPE_CHECKING:
    from models.post import Post


class Tag(Base, CreatedAt):

    name: Mapped[str] = mapped_column(
        Text,
        primary_key=True,
    )
    display_name: Mapped[str] = mapped_column(
        Text,
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates="tags",
        secondary=PostsTagsAssociation.__table__,
    )

    __table_args__ = (
        CheckConstraint(
            func.length(name).between(1, 64),
            name="name_length",
        ),
        UniqueConstraint(display_name),
        CheckConstraint(
            func.length(display_name).between(1, 100),
            name="display_name_length",
        ),
    )

    def __str__(self):
        return self.display_name

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, display_name={self.display_name!r})"
