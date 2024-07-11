from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
    # TODO: raise limits
)


def get_session():
    with Session(engine) as session:
        try:
            yield session
        except SQLAlchemyError:
            session.rollback()
