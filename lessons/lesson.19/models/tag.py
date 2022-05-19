from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .posts_tags import posts_tags_association_table


class Tag(TimestampMixin, Base):
    name = Column(String, unique=True, nullable=False)
    posts = relationship(
        "Post",
        secondary=posts_tags_association_table,
        back_populates="tags",
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr(self.name)
