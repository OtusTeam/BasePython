from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .posts_tags import posts_tags_association


class Post(TimestampMixin, Base):
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    author_id = Column(
        Integer,
        ForeignKey("blog_authors.id"),
        nullable=False,
        unique=False,
    )

    author = relationship("Author", back_populates="posts")

    tags = relationship(
        "Tag",
        secondary=posts_tags_association,
        back_populates="posts",
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(title={self.title!r}, author_id={self.author_id})"
        )
