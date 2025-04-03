from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from models.base import Base
from models.article_source import ArticleSource

if TYPE_CHECKING:
    from .article import Article


class Source(Base):
    __tablename__ = "sources"

    name: Mapped[str] = mapped_column(
        String(300),
    )
    url: Mapped[str] = mapped_column(
        String(4000),
        unique=True,
    )
    articles: Mapped[list["Article"]] = relationship(
        back_populates="sources",
        secondary=ArticleSource.__table__,
    )
    article_associations: Mapped["ArticleSource"] = relationship(
        back_populates="source",
    )

    def __str__(self):
        return self.name
