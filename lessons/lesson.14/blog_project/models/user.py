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

from blog_project.models import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False, server_default="FALSE")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff}, created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)
