# from typing import TYPE_CHECKING
#
# from sqlalchemy import Column
from sqlalchemy import String

# from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from models.db import db
from models.mixins.created_at_mixin import CreatedAtMixin

# if TYPE_CHECKING:
#     from models.post import Post


class User(CreatedAtMixin, db.Model):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    full_name: Mapped[str | None] = mapped_column(String(50), index=True)

    # posts: Mapped[list["Post"]] = relationship(back_populates="author")

    # posts = relationship(
    #     # accessed through `Post.author`
    #     "Post",
    #     back_populates="author",
    #     uselist=True,
    #     # cascade="all, delete-orphan",
    # )
    #
    # profile = relationship(
    #     "UserProfile",
    #     back_populates="user",
    #     uselist=False,
    # )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            "User("
            f"id={self.id}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            ")"
        )
