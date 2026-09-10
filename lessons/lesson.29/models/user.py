from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    func,
    CheckConstraint,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIdentity, CreatedAt

if TYPE_CHECKING:
    from models.post import Post


class User(Base, IdIdentity, CreatedAt):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        Text,
    )
    email: Mapped[str | None] = mapped_column(
        Text,
    )
    full_name: Mapped[str] = mapped_column(
        Text,
        unique=False,
        server_default="",
    )
    posts: Mapped[list[Post]] = relationship(
        back_populates="user",
    )

    __table_args__ = (
        UniqueConstraint(username),
        UniqueConstraint(email),
        CheckConstraint(
            func.length(username) <= 32,
            name="username_length",
        ),
        CheckConstraint(
            func.length(email) <= 200,
            name="email_length",
        ),
        CheckConstraint(
            func.length(full_name) <= 100,
            name="full_name_length",
        ),
    )
