from sqlalchemy import (
    String,
    select,
    create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
)

import config

"""
from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    email: str

    def greet(self):
        return f"Hello, {self.username}!"


john = User(
    id=1,
    username="john",
    email="john@example.com",
)

print(john)
print(john.id)
print(john.username)
print(john.email)
print(john.greet())
"""


engine = create_engine(
    "sqlite:///blog-app.db",
    echo=config.SQLA_DB_ECHO,
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        String(150),
        server_default="",
    )

    def greet(self):
        return f"Hello, {self.username}!"

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", full_name={self.full_name!r})"
        )

    def __repr__(self):
        return str(self)


def insert_values():
    user_john = User(
        username="john",
        email="john@example.com",
    )
    with Session(engine) as session:
        session.add(user_john)
        print("user before commit:", user_john)
        session.commit()
        print("user after commit:", user_john)

    users = [
        User(
            username="bob",
            email="bob@example.com",
            full_name="Bob White",
        ),
        User(
            username="alice",
        ),
    ]
    with Session(engine) as session, session.begin():
        session.add_all(users)


def fetch_values():
    statement = (
        select(User)
        .where(
            User.full_name == "",
            # User.email.is_(None),
            User.email.isnot(None),
            # User.email.is_not(None),
        )
        .order_by(User.id)
    )
    with Session(engine) as session:
        # result = session.execute(statement)
        # users = result.scalars().all()
        users = session.scalars(statement).all()
        for user in users:
            print(user.greet())
            print(user)


def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    insert_values()
    fetch_values()


if __name__ == "__main__":
    main()
