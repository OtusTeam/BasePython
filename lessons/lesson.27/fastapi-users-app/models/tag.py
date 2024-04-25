from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from models.base import Base

from .posts_tags_association import posts_tags_association_table


class Tag(Base):

    name = Column(
        String(32),
        nullable=False,
        unique=True,
    )

    posts = relationship(
        # to tags (class name Post)
        "Post",
        # through this table
        secondary=posts_tags_association_table,
        # access this object through post.tags
        back_populates="tags",
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name!r}"
            f")"
        )
