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


class Post(CreatedAtMixin, Base):
    # _user_back_populates = "posts"

    title = Column(String(100), nullable=False, unique=False)
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
