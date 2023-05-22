from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import (
    relationship,
)

from models import Base

from .mixins import CreatedAtMixin


class Author(CreatedAtMixin, Base):
    name = Column(String(100), nullable=False)
    bio = Column(
        String,
        default="",
        server_default="",
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("blog_users.id"),
        nullable=False,
        unique=True,
    )

    user = relationship(
        "User",
        back_populates="author",
        uselist=False,
    )
    posts = relationship(
        "Post",
        back_populates="author",
        uselist=True,
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r}, user_id={self.user_id})"
