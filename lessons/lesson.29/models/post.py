from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.post_tag_association import post_tag_association_table

if TYPE_CHECKING:
    from models.user import User
    from models.tag import Tag


class Post(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), server_default="")
    text: Mapped[str] = mapped_column(Text, server_default="")
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        # ForeignKey(User.id),
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )
    tags: Mapped[list["Tag"]] = relationship(
        secondary=post_tag_association_table,
        back_populates="posts",
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id!r}"
            f", title={self.title!r}"
            f", text={self.text!r}"
            f", user_id={self.user_id!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)
