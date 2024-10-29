from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

from .mixins.int_pk_mixin import IntPkMixin
from .base import Base

if TYPE_CHECKING:
    from .publication import Publication


class Author(IntPkMixin, Base):
    name: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)

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
