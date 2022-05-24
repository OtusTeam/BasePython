from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import config

engine = create_engine(
    url=config.SQLALCHEMY_DB_URI,
    echo=config.SQLALCHEMY_ECHO,
    pool_size=config.SQLALCHEMY_POOL_SIZE,
    max_overflow=config.SQLALCHEMY_POOL_MAX_OVERFLOW,
)
Session = sessionmaker(bind=engine)
# session_factory = sessionmaker(bind=engine)
# Session = scoped_session(session_factory)
