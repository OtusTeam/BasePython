from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings

engine = create_async_engine(
    settings.db.async_url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)


async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
