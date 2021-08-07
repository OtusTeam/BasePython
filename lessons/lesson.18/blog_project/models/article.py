from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .articles_tags import articles_tags_table
from .mixins import TimestampMixin
from .database import Base
# from .user import User


class Article(TimestampMixin, Base):
    title = Column(String(120), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    status = Column(String(10), nullable=False, default="draft", server_default="draft")

    author_id = Column(Integer, ForeignKey("blog_authors.id"), nullable=False)
    author = relationship("Author", back_populates="articles")

    tags = relationship(
        "Tag",
        secondary=articles_tags_table,
        back_populates="articles",
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title!r}, author_id={self.author_id}, "
            f"tags={self.tags}, created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)
