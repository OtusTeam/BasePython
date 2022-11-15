from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin
from .post_tags import post_tags_association_table


class Tag(CreatedAtMixin, Base):
    name = Column(String(64), unique=True, nullable=False)

    posts = relationship(
        "Post",
        secondary=post_tags_association_table,
        back_populates="tags",
    )

    def __str__(self):
        return f"{self.name}"
