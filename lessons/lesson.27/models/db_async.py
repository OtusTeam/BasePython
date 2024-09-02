from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
import config

engine = create_async_engine(
    url=config.SQLALCHEMY_DATABASE_URI,
    echo=config.SQLALCHEMY_ECHO,
    pool_size=config.SQLALCHEMY_POOL_SIZE,
    max_overflow=config.SQLALCHEMY_MAX_OVERFLOW,
)
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    # autoflush=False,
    # autocommit=False,
)
