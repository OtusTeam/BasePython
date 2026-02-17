from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from config import settings

async_engine = create_async_engine(
    url=settings.db.async_url,
    echo=settings.db.sqla.echo,
    pool_size=settings.db.sqla.pool_size,
    max_overflow=settings.db.sqla.max_overflow,
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)
