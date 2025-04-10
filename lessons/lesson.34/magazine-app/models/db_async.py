from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings

async_engine = create_async_engine(
    url=settings.db.sync_url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)
