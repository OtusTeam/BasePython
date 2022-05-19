from typing import TYPE_CHECKING

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin

if TYPE_CHECKING:
    from .post import Post


class Author(TimestampMixin, Base):
    name = Column(
        String,
        unique=False,
        nullable=False,
        default="",
        server_default="",
    )
    # bio ...

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        unique=True,
    )

    user = relationship("User", back_populates="author")
    posts = relationship("Post", back_populates="author")

    if TYPE_CHECKING:
        posts: list[Post]

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name!r}, "
            f"user_id={self.user_id}"
            # f", user={self.user}"
            ")"
        )
