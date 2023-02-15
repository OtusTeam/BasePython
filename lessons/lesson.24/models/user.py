from uuid import uuid4

from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import relationship

from .base import Base


def generate_token():
    return str(uuid4())


class User(Base):
    username = Column(String(20), unique=True, nullable=False)
    is_staff = Column(Boolean, default=False, nullable=False)
    token = Column(String, unique=True, nullable=False, default=generate_token)

    author = relationship(
        "Author",
        back_populates="user",
        uselist=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"
