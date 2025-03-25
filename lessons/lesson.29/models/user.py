from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    func,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .db import Base

if TYPE_CHECKING:
    from .article import Article


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(32), unique=True)
    full_name: Mapped[str] = mapped_column(
        String(100),
        default="",
        server_default="",
    )
    email: Mapped[str | None] = mapped_column(String(120), unique=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )

    articles: Mapped[list["Article"]] = relationship(
        back_populates="author",
    )

    def __str__(self):
        return self.username


# только чтобы показать, что было сгенерировано.
# это в реальном проекте делать НЕ НУЖНО!
GENERATED_SQL = """
CREATE TABLE users (
	id SERIAL NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	email VARCHAR(120), 
	created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL, 
	CONSTRAINT pk_users PRIMARY KEY (id), 
	CONSTRAINT uq_users_username UNIQUE (username), 
	CONSTRAINT uq_users_email UNIQUE (email)
)"""
