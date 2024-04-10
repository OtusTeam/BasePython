from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship

from models.base import Base


class Post(Base):

    title = Column(
        String(80),
        nullable=False,
        default="",
        server_default="",
    )
    # body = Column(Text, default="", server_default="")
    published_at = Column(
        DateTime(timezone=False),
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

    author = relationship(
        # to class name
        "User",
        # how to access to this model[s]: user.`posts`
        back_populates="posts",
        # author can be only one due to single `user_id`
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"published_at={self.published_at!r}, "
            f"user_id={self.user_id!r}"
            f")"
        )
