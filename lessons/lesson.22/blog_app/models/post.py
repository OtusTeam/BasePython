from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .posts_tags import posts_tags_table


class Post(TimestampMixin, Base):
    title = Column(String(256), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    author_id = Column(Integer, ForeignKey("blog_app__users.id"), nullable=True)

    author = relationship("User", back_populates="posts")
    tags = relationship(
        "Tag",
        secondary=posts_tags_table,
        back_populates="posts",
    )
