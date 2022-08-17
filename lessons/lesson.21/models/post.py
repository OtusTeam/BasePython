from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, ForeignKey, Text

from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .post_tags import post_tags_association_table

if TYPE_CHECKING:
    from .tag import Tag


class Post(TimestampMixin, Base):
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="N/A")

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="posts")

    tags = relationship(
        "Tag", secondary=post_tags_association_table, back_populates="posts"
    )

    if TYPE_CHECKING:
        tags: list["Tag"]

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author_id={self.author_id})"
