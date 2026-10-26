from uuid import UUID
from uuid import uuid7

from sqlalchemy import CheckConstraint
from sqlalchemy import String
from sqlalchemy import false
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from bookshelf.core.db import Base
from bookshelf.core.db import CreatedAtMixin


class Book(CreatedAtMixin, Base):
    __table_args__ = (
        CheckConstraint("length(trim(title)) BETWEEN 1 AND 100", name="title_length"),
        CheckConstraint("pages BETWEEN 1 AND 10000", name="pages_range"),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)
    title: Mapped[str] = mapped_column(String(100))
    pages: Mapped[int]
    is_read: Mapped[bool] = mapped_column(default=False, server_default=false())
