from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config


engine = create_engine(
    config.SQLA_PG_URL,
    echo=config.SQLA_ECHO,
)

session_factory = sessionmaker(bind=engine)
