from typing import TYPE_CHECKING

from sqlalchemy import (
    Column,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship
from uuid import uuid4

from .base import Base
from .mixins import TimestampMixin


if TYPE_CHECKING:
    from .author import Author


def generate_token():
    token = str(uuid4())
    print("new token", token)
    return token


class User(TimestampMixin, Base):
    username = Column(String(20), unique=True)
    is_staff = Column(Boolean, default=False, server_default="FALSE")
    token = Column(String, default=generate_token, nullable=False)

    author = relationship("Author", back_populates="user", uselist=False)

    if TYPE_CHECKING:
        author: Author

    def __init__(self, username: str, is_staff: bool = False):
        super(User, self).__init__()
        self.username = username
        self.is_staff = is_staff

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}"
            f", is_staff={self.is_staff}, "
            f"created_at={self.created_at}"
            ")"
        )
