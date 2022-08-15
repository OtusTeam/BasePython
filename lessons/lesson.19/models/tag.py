from sqlalchemy import Column, String

from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin
from .post_tags import post_tags_association_table


class Tag(TimestampMixin, Base):
    name = Column(String(20), unique=True, nullable=False)

    posts = relationship(
        "Post", secondary=post_tags_association_table, back_populates="tags"
    )
