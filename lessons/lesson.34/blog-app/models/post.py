from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.mixins.created_at import CreatedAtMixin
from models.mixins.id_int_pk import IdIntPkMixin
from models.posts_tags import PostTagsAssociation

if TYPE_CHECKING:
    from models import User, Tag


class Post(
    IdIntPkMixin,
    CreatedAtMixin,
    Base,
):
    title: Mapped[str] = mapped_column(
        String(100),
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
        secondary=PostTagsAssociation.__table__,
    )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, user_id={self.user_id!r})"

    def __repr__(self) -> str:
        return str(self)
