from sqlalchemy import (
    String,
    create_engine,
    select,
    func,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
)


import config

engine = create_engine(
    url=config.SQLA_SQLITE_DB_URL,
    echo=config.SQLA_DB_ECHO,
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(String(150), unique=True)
    full_name: Mapped[str] = mapped_column(String(100), server_default="")

    def greet(self) -> str:
        return f"Hello, {self.username}!"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", full_name={self.full_name!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_values() -> None:
    user_john = User(
        username="john",
        email="john@example.com",
        full_name="John Smith",
    )
    print("creating user", user_john)

    with Session(engine) as session:
        session.add(user_john)
        session.commit()
        print("committed user")

        print("the user:", user_john)
        print("lalala")
        print("the user (again):", user_john)
    print("the user (againagainagain):", user_john)

    # ###

    user_alice = User(
        username="alice",
    )
    user_bob = User(
        username="bob",
        email="bob@example.com",
    )

    users = [user_alice, user_bob]
    with Session(engine) as session:
        session.add_all(users)
        session.commit()

        print("all users:", users)


def fetch_values() -> None:
    statement = select(User).order_by(User.id)
    with Session(engine) as session:
        users = session.scalars(statement).all()

    for user in users:
        print("-", user)

    print("---")
    statement = (
        select(User)
        .where(
            # User.email.is_(None),
            User.email.isnot(None),
            func.length(User.username) >= 3,
            # func.length(User.username) > 2,
            # func.length(User.username) > 3,
        )
        .order_by(User.id)
    )
    with Session(engine) as session:
        users = session.scalars(statement).all()

    for user in users:
        print(user.greet())
        print("-", user)


def main() -> None:
    # create_tables()
    # insert_values()
    fetch_values()


# чисто для информации!
# мы в реальности не копируем это сюда в код!
# это только для демо - что было АВТОМАТИЧЕСКИ сгенерировано из нашего кода.

"""\
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""

if __name__ == "__main__":
    main()
