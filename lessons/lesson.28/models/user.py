from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    func,
    CheckConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIdentity

if TYPE_CHECKING:
    from models.post import Post


class User(Base, IdIdentity):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        Text,
        unique=True,
    )

    email: Mapped[str | None] = mapped_column(
        Text,
        unique=True,
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
        CheckConstraint(func.length(username) <= 32),
        CheckConstraint(func.length(email) <= 200),
        CheckConstraint(func.length(full_name) <= 100),
    )
