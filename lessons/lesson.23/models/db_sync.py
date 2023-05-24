from sqlalchemy import (
    create_engine,
)

from sqlalchemy.orm import (
    Session,
)


import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
    pool_size=config.DB_POOL_SIZE,
    max_overflow=config.DB_MAX_OVERFLOW,
)


def get_session() -> Session:
    with Session(engine) as session:  # type: Session
        yield session
        # cleanup. OPTIONAL!
        session.rollback()
