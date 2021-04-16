from datetime import datetime
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    create_engine,
    func,
)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///example-03.db", echo=True)

Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False, server_default="0")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())


if __name__ == '__main__':
    Base.metadata.create_all()
