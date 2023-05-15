from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    relationship,
)

from models import Base

from .mixins import CreatedAtMixin
from .posts_tags import posts_tags_association_table


class Post(CreatedAtMixin, Base):
    title = Column(
        String(90),
        nullable=False,
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    author_id = Column(
        Integer,
        ForeignKey("blog_authors.id"),
        unique=False,
        nullable=False,
    )
    author = relationship(
        "Author",
        back_populates="posts",
        uselist=False,
    )
    tags = relationship(
        "Tag",
        secondary=posts_tags_association_table,
        back_populates="posts",
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author_id={self.author_id})"

    def __repr__(self):
        return str(self)