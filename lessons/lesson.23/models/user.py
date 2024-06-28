from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base

if TYPE_CHECKING:
    from .post import Post


class User(Base):

    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="author")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email!r}"
            ")"
        )
