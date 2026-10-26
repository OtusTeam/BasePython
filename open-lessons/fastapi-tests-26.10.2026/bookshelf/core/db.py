from contextlib import contextmanager
from datetime import datetime  # noqa: TC003 - SQLAlchemy resolves Mapped annotations at runtime.
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import mapped_column


if TYPE_CHECKING:
    from collections.abc import Generator

    from sqlalchemy.engine import Engine

    from bookshelf.config.settings import Settings


class Base(DeclarativeBase):
    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:  # pyrefly: ignore[bad-override]
        # shortcut: Book is the only model; extend pluralization when adding other names.
        return f"{cls.__name__.lower()}s"

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(table_name)s_%(column_0_name)s",
            "uq": "uq_%(table_name)s_%(column_0_N_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


@contextmanager
def managed_engine(settings: Settings) -> Generator[Engine]:
    engine = create_engine(settings.database.url, connect_args={"check_same_thread": False})
    try:
        yield engine
    finally:
        engine.dispose()
