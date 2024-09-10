from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
    pool_size=config.SQLA_POOL_SIZE,
    max_overflow=config.SQLA_MAX_OVERFLOW,
)


def get_session():
    with Session(engine) as session:
        try:
            yield session
        except SQLAlchemyError:
            session.rollback()
