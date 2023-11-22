from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import config

engine = create_engine(
    url=config.DB_SYNC_URL,
    echo_pool=config.DB_ECHO,
    pool_size=config.DB_POOL_SIZE,
    max_overflow=config.DB_MAX_OVERFLOW,
)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
