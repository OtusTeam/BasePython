from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    declared_attr,
    Session as SessionType,
)

from blog_project import config


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(
    config.SQLA_CONN_URI,
    echo=config.SQLA_ECHO,
    pool_size=config.SQLA_POOL_SIZE,
    max_overflow=config.SQLA_MAX_OVERFLOW,
)
Base = declarative_base(bind=engine, cls=Base)


session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def session_dependency() -> SessionType:
    session: SessionType = Session()
    yield session
    # session.rollback()
    session.close()
