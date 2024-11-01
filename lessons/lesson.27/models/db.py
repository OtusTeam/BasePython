from sqlalchemy import create_engine

import config

engine = create_engine(
    url=config.SQLALCHEMY_DATABASE_URI,
    echo=config.SQLALCHEMY_ECHO,
)
