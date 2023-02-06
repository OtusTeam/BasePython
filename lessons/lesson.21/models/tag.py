from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .posts_tags import posts_tags_association


class Tag(TimestampMixin, Base):
    name = Column(String(20), nullable=False, unique=True)

    posts = relationship(
        "Post",
        secondary=posts_tags_association,
        back_populates="tags",
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"
