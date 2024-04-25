from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from models.db import engine
from models.db_async import async_session


def get_session() -> Session:
    with Session(engine) as session:
        try:
            yield session
        finally:
            # optional!! cleanup
            session.rollback()


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        # yield session
        try:
            yield session
        finally:
            # optional!! cleanup
            await session.rollback()
