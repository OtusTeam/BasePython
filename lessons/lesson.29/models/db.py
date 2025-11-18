from sqlalchemy import create_engine

import config

engine = create_engine(
    url=config.SQLA_URL,
    echo=config.SQLA_ECHO,
)
