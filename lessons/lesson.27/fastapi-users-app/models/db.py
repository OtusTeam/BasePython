from sqlalchemy import create_engine

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
    # pool_pre_ping=True,
    pool_size=config.DB_POOL_SIZE,
    max_overflow=config.DB_MAX_OVERFLOW,
)
