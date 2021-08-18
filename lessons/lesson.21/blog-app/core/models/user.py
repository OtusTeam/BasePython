from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    Boolean,
)

from .mixins import TimestampMixin
from .base import Base


class User(TimestampMixin, Base):

    @classmethod
    def generate_token(cls):
        token = str(uuid4())
        print("Create Token", token)
        return token

    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    auth_token = Column(String(36), unique=True, nullable=False, index=True)

    def __init__(self, username: str, is_staff: bool = False):
        self.username = username
        self.is_staff = is_staff
        self.auth_token = self.generate_token()

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username!r}, is_staff={self.is_staff}, "
            f"created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)
