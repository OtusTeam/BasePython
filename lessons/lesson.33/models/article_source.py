from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint, Identity, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

if TYPE_CHECKING:
    from .article import Article
    from .source import Source


class ArticleSource(Base):
    __tablename__ = "article_source_association_table"

    id: Mapped[int] = mapped_column(
        Identity(always=True),
        primary_key=True,
    )

    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id"),
    )
    source_id: Mapped[int] = mapped_column(
        ForeignKey("sources.id"),
    )

    details: Mapped[str] = mapped_column(
        String(200),
        default="",
        server_default="",
    )

    article: Mapped["Article"] = relationship(
        back_populates="source_associations",
    )
    source: Mapped["Source"] = relationship(
        back_populates="article_associations",
    )

    __table_args__ = (
        UniqueConstraint(
            article_id,
            source_id,
        ),
    )
