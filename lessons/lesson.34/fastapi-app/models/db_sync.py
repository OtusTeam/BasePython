from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    config.db_url,
    # echo=True only for debug!!
    echo=config.db_echo,
    pool_size=config.db_pool_size,
    max_overflow=config.db_max_overflow,
)

session_factory = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
