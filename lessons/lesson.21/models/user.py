from uuid import uuid4

from sqlalchemy import (
    Column,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


def generate_token() -> str:
    token = str(uuid4())
    print(token)
    return token


class User(CreatedAtMixin, Base):
    username = Column(String(20), unique=True)
    archived = Column(
        Boolean,
        default=False,
        # nullable=False,
    )
    token = Column(
        String(64),
        nullable=True,
        unique=True,
        default=generate_token,
    )

    # orm
    author = relationship("Author", back_populates="user", uselist=False)

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"
