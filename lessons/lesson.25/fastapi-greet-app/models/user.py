from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import String

from sqlalchemy.orm import relationship

from models.base import Base
from models.mixins.created_at_mixin import CreatedAtMixin


def generate_token() -> str:
    token = str(uuid4())
    print("New user token:", token)
    return token


class User(CreatedAtMixin, Base):
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    full_name = Column(String(50), nullable=True, index=True)
    token = Column(
        String(36),
        nullable=True,
        unique=True,
        default=generate_token,
    )

    posts = relationship(
        # accessed through `Post.author`
        "Post",
        back_populates="author",
        uselist=True,
        # cascade="all, delete-orphan",
    )

    profile = relationship(
        "UserProfile",
        back_populates="user",
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            "User("
            f"id={self.id}"
            f", username={self.username!r}"
            # f", email={self.email!r}"
            ")"
        )
