from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from models.base import Base


class Post(Base):
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    # body = Column(Text, nullable=False)
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
    author = relationship(
        # accessed through `User.posts`
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"Post(id={self.id}, "
            f"title={self.title!r}, "
            f"published_at={self.published_at!r}, "
            f"user_id={self.user_id})"
        )
