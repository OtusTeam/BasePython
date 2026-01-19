from sqlalchemy import create_engine

import config

engine = create_engine(
    url=config.SQLA_DB_URL,
    echo=config.SQLA_DB_ECHO,
)
