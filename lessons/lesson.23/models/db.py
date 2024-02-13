from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from config import DB_URL, DB_ECHO

# engine = create_async_engine(
async_engine = create_async_engine(
    DB_URL,
    echo=DB_ECHO,
)
# async_session = sessionmaker(
#     ...,
#     class_=AsyncSession,
# )
async_session = async_sessionmaker(
    bind=async_engine,
    # class_=AsyncSession,
    autocommit=False,
    expire_on_commit=False,
)
