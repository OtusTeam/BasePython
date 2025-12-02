from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    url=config.SQLA_URL,
    echo=config.SQLA_ECHO,
    pool_size=config.SQLA_POOL_SIZE,
    max_overflow=config.SQLA_MAX_OVERFLOW,
)

session_factory = sessionmaker(
    bind=engine,
)
