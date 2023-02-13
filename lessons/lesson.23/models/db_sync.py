from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session,
)

import config

engine = create_engine(url=config.DB_URL, echo=config.DB_ECHO)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
