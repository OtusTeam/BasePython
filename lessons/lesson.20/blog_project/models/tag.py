from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from .articles_tags import articles_tags_table
from .mixins import TimestampMixin
from .database import Base


class Tag(TimestampMixin, Base):
    name = Column(String(32), unique=True, nullable=False)

    articles = relationship(
        "Article",
        secondary=articles_tags_table,
        back_populates="tags",
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
