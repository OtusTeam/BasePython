from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.mixins import CreatedAtMixin

if TYPE_CHECKING:
    from models import User


class Post(CreatedAtMixin, Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(
        String(100),
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )


# этот код сгенерирован, мы его не набираем вручную!
GENERATED_SQL = """
CREATE TABLE posts (
	title VARCHAR(100) NOT NULL, 
	body TEXT DEFAULT '' NOT NULL, 
	user_id INTEGER NOT NULL, 
	created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL, 
	id SERIAL NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);
"""
