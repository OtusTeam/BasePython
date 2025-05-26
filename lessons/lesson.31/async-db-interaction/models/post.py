from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base import Base

# from models.post_tag_association import posts_tags_association
from models.post_tag_association import PostTagAssociation
from models.mixins import CreatedAtMixin

if TYPE_CHECKING:
    from models import User, Tag


class Post(CreatedAtMixin, Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(
        String(120),
        index=True,
        default="",
        server_default="",
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )
    tags: Mapped[list["Tag"]] = relationship(
        back_populates="posts",
        # secondary=posts_tags_association,
        secondary=PostTagAssociation.__table__,
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user_id={self.user_id!r})"

    def __repr__(self) -> str:
        return str(self)
