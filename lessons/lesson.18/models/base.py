from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)

Base = declarative_base()
