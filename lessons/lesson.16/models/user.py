from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship

from .mixins import TimestampMixin
from .database import Base
# from models.database import Base


class User(TimestampMixin, Base):

    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)

    author = relationship("Author", back_populates="user", uselist=False)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username!r}, is_staff={self.is_staff}, "
            f"created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)
