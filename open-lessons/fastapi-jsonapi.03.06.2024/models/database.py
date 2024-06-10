from sqlalchemy import (
    make_url,
    Integer,
    Column,
)
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import (
    DB_URL,
    DB_ECHO,
)


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)


def create_engine():
    return create_async_engine(
        url=make_url(DB_URL),
        echo=DB_ECHO,
    )


async def sqlalchemy_init() -> None:
    engine = create_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
