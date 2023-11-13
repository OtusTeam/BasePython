from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)

from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin
from .posts_tags_association import posts_tags_association_table


class Tag(CreatedAtMixin, Base):
    name = Column(
        String(20),
        nullable=False,
        unique=True,
    )

    posts = relationship(
        "Post",
        secondary=posts_tags_association_table,
        back_populates="tags",
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Tag(id={self.id}, name={self.name!r})"
