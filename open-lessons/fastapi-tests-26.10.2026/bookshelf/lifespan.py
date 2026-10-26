from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from sqlalchemy.orm import sessionmaker

from bookshelf.books.models import Book  # noqa: F401 - Register the model in Base.metadata.
from bookshelf.core.db import Base
from bookshelf.core.db import managed_engine


if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    with managed_engine(app.state.settings) as engine:
        # shortcut: one fixed teaching schema; use migrations when the schema starts evolving.
        Base.metadata.create_all(engine)
        app.state.engine = engine
        app.state.sessionmaker = sessionmaker(engine, expire_on_commit=False)
        yield
