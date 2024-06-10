from sqlalchemy.ext.asyncio import async_sessionmaker

from models.database import create_engine


def async_session() -> async_sessionmaker:
    engine = create_engine()
    _async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
    return _async_session


class Connector:
    @classmethod
    async def get_session(cls):
        """
        Get session as dependency
        """
        sess = async_session()
        async with sess() as db_session:
            yield db_session
            await db_session.rollback()
