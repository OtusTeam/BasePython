from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import db_url, db_echo

engine = create_async_engine(
    db_url,
    # echo=True only for debug!!
    echo=db_echo,
)


async_session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
