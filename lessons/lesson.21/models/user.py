from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from models.base import Base


class User(Base):

    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)

    posts = relationship(
        # to class name
        "Post",
        # how to access to this model[s]: post.`author`
        back_populates="author",
        # user can have any number of posts
        uselist=True,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email!r}"
            f")"
        )
