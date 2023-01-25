from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)
from sqlalchemy.orm import DeclarativeBase

DB_URL = 'sqlite:///users.sqlite3'
# DB_URL = 'postgresql+pg8000://username:passwd@localhost:5432/users' #psycopg2
DB_ECHO = True

engine = create_engine(url=DB_URL, echo=DB_ECHO)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    is_staff = Column(Boolean, default=False, nullable=True)
    create_at = Column(DateTime, default=datetime.utcnow())
    # is_active = Column(Boolean, default=True, nullable=True)


def create_database():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_database()