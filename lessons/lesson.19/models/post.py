from sqlalchemy import Column, String, Integer, ForeignKey, Text

from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .post_tags import post_tags_association_table


class Post(TimestampMixin, Base):
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="N/A")
    # 1 - 1
    # 1 - *
    # * - *

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="posts", uselist=True)

    tags = relationship(
        "Tag", secondary=post_tags_association_table, back_populates="posts"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(" f"id={self.id} " f"title={self.title} )"
