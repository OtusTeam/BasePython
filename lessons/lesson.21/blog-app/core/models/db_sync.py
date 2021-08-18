from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, declared_attr

from .base import Base

engine = create_engine("postgresql://user:password@localhost:5432/blog_project", echo=False)
Base = declarative_base(bind=engine, cls=Base)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def get_sync_session():
    session = Session()
    yield session
    session.close()

