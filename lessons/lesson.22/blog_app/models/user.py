from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin


class User(TimestampMixin, Base):

    @classmethod
    def generate_token(cls):
        token = str(uuid4())
        print("Created token", repr(token))
        return token

    def __init__(self, username: str, is_staff: bool = False):
        self.username = username
        self.is_staff = is_staff
        self.access_token = self.generate_token()

    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    access_token = Column(
        String(36),
        unique=True,
        nullable=True,
        index=True,
    )

    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, " \
               f"username={self.username!r}, is_staff={self.is_staff})"
