from sqlalchemy import (
    create_engine,
    Column,
    Integer,
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    declared_attr,
)

import config


class Base:
    @declared_attr
    def __tablename__(cls):
        # users
        # authors
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
    pool_size=config.DB_POOL_SIZE,
    max_overflow=config.DB_MAX_OVERFLOW,
)
Base = declarative_base(bind=engine, cls=Base)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
