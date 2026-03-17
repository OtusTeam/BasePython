from typing import TYPE_CHECKING

from sqlalchemy import (
    Text,
    CheckConstraint,
    func,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import IdIntPk

if TYPE_CHECKING:
    from models import Post


class User(IdIntPk, Base):

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
        default="",
        server_default="",
    )
    posts: Mapped[list[Post]] = relationship(
        back_populates="user",
    )

    __table_args__ = (
        CheckConstraint(
            func.length(username) <= 32,
            name="username_max_length",
        ),
        CheckConstraint(
            func.length(full_name) <= 100,
            name="full_name_max_length",
        ),
    )

    def greet(self) -> str:
        return f"Hello, {self.username}!"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", full_name={self.full_name!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)
