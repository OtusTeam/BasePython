from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin


class AuthorBio(TimestampMixin, Base):
    text = Column(Text, nullable=False, default="", server_default="")

    author_id = Column(
        Integer,
        ForeignKey("blog_authors.id"),
        nullable=False,
        unique=True,
    )
    author = relationship(
        "Author",
        back_populates="bio",
        uselist=False,
    )
