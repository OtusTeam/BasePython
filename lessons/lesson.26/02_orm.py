from datetime import datetime
from email.policy import default
from pathlib import Path

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    insert,
    select,
    func,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
)

BASE_DIR = Path(__file__).parent
SQLITE_DB_FILE = BASE_DIR / "blog.db"

# enable for debug
ECHO = True
# ECHO = False
engine = create_engine(
    url="sqlite:///:memory:",
    # url=f"sqlite:///{SQLITE_DB_FILE}",
    echo=ECHO,
)


class Base(DeclarativeBase):
    pass


# не для выполнения, только для примера!
SQLITE_GENERATED = """
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	full_name VARCHAR DEFAULT '' NOT NULL, 
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(length=32),
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        String(length=150),
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        default="",
        server_default="",
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )


def create_users() -> None:
    bob = User(
        username="bob",
        email="bob@example.com",
        created_at=datetime.utcnow(),
    )
    alice = User(
        username="alice",
        email="alice@example.com",
    )
    john = User(
        username="john",
        full_name="John Smith",
    )
    with Session(engine, expire_on_commit=False) as session:
        session.add(bob)
        print("bob", bob.id, "'created at' before commit", bob.created_at)
        session.commit()
        print("bob", bob.id, "'created at' after commit", bob.created_at)

        session.add(alice)
        session.add(john)
        session.commit()


def main() -> None:
    print(Base.metadata.tables)
    print(repr(User.__table__))
    Base.metadata.create_all(engine)
    create_users()


if __name__ == "__main__":
    main()
