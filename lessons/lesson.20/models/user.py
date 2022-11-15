from sqlalchemy import (
    Column,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


# class User(Base):
class User(CreatedAtMixin, Base):
    username = Column(String(20), unique=True)
    archived = Column(
        Boolean,
        default=False,
        # nullable=False,
    )

    # orm
    author = relationship("Author", back_populates="user", uselist=False)

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"
