from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session,
    declarative_base,
    declared_attr,
)

import config


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> blog_users
        Author -> blog_authors
        """
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine(url=config.DB_URL, echo=config.DB_ECHO)

Base = declarative_base(cls=Base, bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
