import secrets
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

from .mixins.int_pk_mixin import IntPkMixin
from .base import Base

if TYPE_CHECKING:
    from .publication import Publication


def generate_promocode():
    return secrets.token_urlsafe(8)


class Author(IntPkMixin, Base):
    name: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    promocode: Mapped[str] = mapped_column(
        unique=True,
        # pass callable
        default=generate_promocode,
    )
    joined_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )

    publications: Mapped[list["Publication"]] = relationship(
        back_populates="author",
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f" name={self.name!r},"
            f" username={self.username!r},"
            f" email={self.email!r}"
            f")"
        )

    def __repr__(self) -> str:
        return str(self)
