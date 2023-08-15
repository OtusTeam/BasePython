from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Text,
    func,
)

from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin
from .posts_tags_association import posts_tags_association_table


class Post(CreatedAtMixin, Base):
    # _user_back_populates = "posts"

    title = Column(
        String(120),
        nullable=False,
        unique=False,
        # index=True,
    )
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )

    published_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    tags = relationship(
        "Tag",
        secondary=posts_tags_association_table,
        back_populates="posts",
        # uselist=True,
    )

    @property
    def body_len(self):
        return len(self.body)

    def __str__(self):
        return f"Post(id={self.id}, title={self.title!r})"

    def __repr__(self):
        """
        :return:
        """
        return str(self)
