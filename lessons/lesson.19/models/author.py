from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin


class Author(TimestampMixin, Base):
    name = Column(
        String(80),
        unique=False,
        nullable=False,
        default="",
        server_default="",
    )
    user_id = Column(
        Integer,
        ForeignKey("blog_users.id"),
        nullable=False,
        unique=True,
        # ForeignKey(User.id)
    )

    user = relationship(
        "User",
        back_populates="author",
        uselist=False,
    )
    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.name}(name={self.name!r}, user_id={self.user_id})"
