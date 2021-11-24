from sqlalchemy import (
    Column,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import TimestampMixin


class User(TimestampMixin, Base):

    def __init__(self, username: str, is_staff: bool = False):
        self.username = username
        self.is_staff = is_staff

    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)

    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, " \
               f"username={self.username!r}, is_staff={self.is_staff})"
