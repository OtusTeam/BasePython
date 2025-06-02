import random
import string
from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.mixins import CreatedAtMixin

if TYPE_CHECKING:
    from models import Post, UserStatus


def new_friend_code():
    return "".join(random.choices(string.ascii_letters, k=8))


class User(CreatedAtMixin, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        String(length=32),
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        String(length=150),
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        default="",
        server_default="",
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )
    friend_code: Mapped[str] = mapped_column(
        String(length=20),
        unique=True,
        default=new_friend_code,
    )
    status: Mapped[str | None] = mapped_column(
        ForeignKey("user_status.name"),
    )
    # users_status: Mapped["UserStatus | None"] = relationship(
    #     back_populates="users"
    # )

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, email={self.email!r})"

    def __repr__(self) -> str:
        return str(self)
