from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session,
    Session as SessionType,
)

import config

engine = create_engine(
    url=config.DB_SYNC_URL,
    echo=config.DB_ECHO,
    max_overflow=config.MAX_OVERFLOW,
    pool_size=config.POOL_SIZE,
)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def get_session() -> SessionType:
    with Session() as session:
        yield session
