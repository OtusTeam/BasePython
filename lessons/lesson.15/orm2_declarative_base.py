from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime, false,
)

from sqlalchemy.orm import declarative_base

DB_URL = "sqlite:///example2.db"
# optional!!
DB_ECHO = True
# DB_ECHO = False
engine = create_engine(url=DB_URL, echo=DB_ECHO)

Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    archived = Column(Boolean, default=False, server_default=false())
    created_at = Column(DateTime, default=datetime.utcnow)


def main():
    sql = """
    CREATE TABLE users (
        id INTEGER NOT NULL, 
        username VARCHAR(20), 
        archived BOOLEAN DEFAULT (0), 
        created_at DATETIME, 
        PRIMARY KEY (id), 
        UNIQUE (username)
    );
    """

    Base.metadata.drop_all()
    Base.metadata.create_all()


if __name__ == "__main__":
    main()
