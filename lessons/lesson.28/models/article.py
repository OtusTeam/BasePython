from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    func,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .db import Base

if TYPE_CHECKING:
    from .user import User


class Article(Base):
    __tablename__ = "articles"

    title: Mapped[str] = mapped_column(
        String(140),
        default="",
        server_default="",
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    published_at: Mapped[datetime | None] = mapped_column(
        DateTime,
    )
    author_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
    )

    author: Mapped["User"] = relationship(
        back_populates="articles",
    )


# только чтобы показать, что было сгенерировано.
# это в реальном проекте делать НЕ НУЖНО!
GENERATED_SQL = """
CREATE TABLE articles (
	id SERIAL NOT NULL, 
	title VARCHAR(120) DEFAULT '' NOT NULL, 
	body TEXT DEFAULT '' NOT NULL, 
	published_at TIMESTAMP WITHOUT TIME ZONE, 
	author_id INTEGER NOT NULL, 
	CONSTRAINT pk_articles PRIMARY KEY (id), 
	CONSTRAINT fk_articles_author_id_users
	    FOREIGN KEY(author_id) 
	        REFERENCES users (id)
	            ON DELETE CASCADE
)
"""
