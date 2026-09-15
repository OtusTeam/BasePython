from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    func,
    CheckConstraint,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.posts_tags_association import PostsTagsAssociation
from models.base import Base

from models.mixins import IdIdentity, CreatedAt

if TYPE_CHECKING:
    from models import Tag, User


class Post(Base, IdIdentity, CreatedAt):

    title: Mapped[str] = mapped_column(
        Text,
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            # ondelete="RESTRICT",
        ),
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )
    tags: Mapped[list["Tag"]] = relationship(
        back_populates="posts",
        secondary=PostsTagsAssociation.__table__,
    )

    __table_args__ = (
        #
        CheckConstraint(
            func.length(title) <= 80,
            name="title_length",
        ),
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user_id={self.user_id!r})"
