import uuid

from sqlalchemy import (
    Column,
    String,
    Boolean,
    false,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


class BaseUser(CreatedAtMixin, Base):
    __abstract__ = True

    username = Column(String(32), nullable=False, unique=True)
    email = Column(String(120), nullable=True, unique=True)
    is_staff = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default=false(),
    )


class User(BaseUser):
    def __init__(self, **kwargs):
        self.token = self.generate_token()
        super().__init__(**kwargs)

    @classmethod
    def generate_token(cls):
        token = str(uuid.uuid4())
        print("New token", token)
        return token

    token = Column(
        String(50),
        nullable=True,
        unique=True,
    )
    bio = Column(
        String(200),
        nullable=True,
        unique=False,
    )

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, email={self.email!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)


class Manager(BaseUser):
    foobar = Column(String, unique=True)
