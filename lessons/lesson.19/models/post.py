from datetime import datetime

from sqlalchemy import Column, UniqueConstraint
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.orm import relationship

from models.base import Base


class Post(Base):
    __table_args__ = (
        UniqueConstraint("title", "published_at"),
    )

    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
        # index=True,
    )
    # body = Column(Text...)

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
    # __table_args__ = (
    #     UniqueConstraint(
    #     title,
    #     published_at,
    #     )
    # )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title!r}, user_id={self.user_id!r})"
        )

    def __repr__(self):
        return str(self)
