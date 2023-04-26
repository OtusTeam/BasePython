from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    false,
    DateTime,
    func,
)
from sqlalchemy.orm import (
    relationship,
)

from models import Base


class User(Base):
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(180), unique=True)
    archived = Column(
        Boolean,
        default=False,
        server_default=false(),
        nullable=False,
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )

    author = relationship(
        "Author",
        back_populates="user",
        uselist=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, created_at={self.created_at})"

    def __repr__(self):
        return str(self)
