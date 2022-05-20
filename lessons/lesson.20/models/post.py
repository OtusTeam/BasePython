from typing import TYPE_CHECKING

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .posts_tags import posts_tags_association_table

if TYPE_CHECKING:
    from .author import Author
    from .tag import Tag


class Post(TimestampMixin, Base):
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")

    author_id = Column(
        Integer,
        ForeignKey("authors.id"),
        nullable=False,
        unique=False,
    )
    author = relationship("Author", back_populates="posts")
    tags = relationship(
        "Tag",
        secondary=posts_tags_association_table,
        back_populates="posts",
    )

    if TYPE_CHECKING:
        author: Author
        tags: list[Tag]

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"author_id={self.author_id}, "
            f"created_at={self.created_at}"
            ")"
        )
