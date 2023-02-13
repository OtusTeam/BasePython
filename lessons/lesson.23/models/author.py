from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin


class Author(TimestampMixin, Base):
    name = Column(
        String(160),
        unique=False,
        nullable=False,
        default="",
        server_default="",
    )
    user_id = Column(
        Integer,
        ForeignKey("blog_users.id", name="fk_user_id"),
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

    bio = relationship(
        "AuthorBio",
        back_populates="author",
        uselist=False,
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r}, user_id={self.user_id})"
