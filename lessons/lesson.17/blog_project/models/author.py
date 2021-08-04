from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .mixins import TimestampMixin
from .database import Base
# from .user import User


class Author(TimestampMixin, Base):
    name = Column(String(64), nullable=False, default="", server_default="")
    bio = Column(String(300), nullable=False, default="", server_default="")
    user_id = Column(Integer, ForeignKey("blog_users.id"), nullable=False, unique=True)
    # user_id = Column(Integer, nullable=False, unique=True)
    user = relationship("User", back_populates="author")
    articles = relationship("Article", back_populates="author")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"name={self.name!r}, user_id={self.user_id}, "
            f"created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)
