from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(
    url=config.SQLALCHEMY_DATABASE_URI,
    echo=config.SQLALCHEMY_ECHO,
)

session_factory = sessionmaker(
    bind=engine,
    # autoflush=False,
    # autocommit=False,
    # expire_on_commit=False,
)
