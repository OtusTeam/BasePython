from sqlalchemy import (
    Column,
    String,
    Boolean,
    false,
)
from sqlalchemy.orm import (
    relationship,
)

from models import Base

from .mixins import CreatedAtMixin


class User(CreatedAtMixin, Base):
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(180), unique=True)
    archived = Column(
        Boolean,
        default=False,
        server_default=false(),
        # server_default="FALSE",
        # server_default="0",
        nullable=False,
    )

    # bio = Column(
    #     String,
    #     default="",
    #     server_default="",
    #     nullable=False,
    # )

    author = relationship(
        "Author",
        back_populates="user",
        uselist=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, created_at={self.created_at})"

    def __repr__(self):
        return str(self)
