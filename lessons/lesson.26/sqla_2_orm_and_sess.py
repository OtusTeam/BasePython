from sqlalchemy import (
    select,
    func,
    String,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    DeclarativeBase,
    Session,
)

engine = create_engine(
    "sqlite:///blog.db",
    echo=True,
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
    )
    email: Mapped[str | None] = mapped_column(
        String(150),
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )

    def greet(self) -> str:
        return f"Hello, {self.username}!"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, email={self.email!r}, full_name={self.full_name!r})"

    def __repr__(self) -> str:
        return str(self)


def insert_one():
    with Session(engine) as session:
        user = User(
            username="bob",
            email="bob@example.com",
            full_name="Bob White",
        )
        session.add(user)
        print("user before commit:", user)
        session.commit()
        print("user after commit:", user)


def insert_many() -> None:
    # alice = User(
    #     username="alice",
    #     full_name="Alice White",
    # )
    # john = User(
    #     username="john",
    # )
    kate = User(
        username="kate",
        full_name="Kate Brown",
    )
    kyle = User(
        username="kyle",
        full_name="",
    )

    users = [
        # alice,
        # john,
        kate,
        kyle,
    ]
    with Session(engine) as session:
        session.add_all(users)
        session.commit()


def select_users():
    statement = select(User).order_by(User.id)
    with Session(engine) as session:
        result = session.execute(statement)
        for user in result.scalars():  # type: User
            print(user.greet(), user)


def main() -> None:
    # print(repr(User.__table__))
    # print(Base.metadata.tables)
    # Base.metadata.create_all(engine)

    statement = select(User).where(User.username == "kate")
    with Session(engine) as session:
        result = session.execute(statement)
        user: User = result.scalar_one()
        print(user.greet(), user)
        user.email = "kate@example.com"
        session.commit()

    statement = (
        select(User)
        .where(
            User.email.is_not(None),
            func.length(User.username) > 3,
        )
        .order_by(User.id)
    )
    with Session(engine) as session:
        result = session.scalars(statement)
        for user in result:  # type: User
            print(user.greet(), user)


if __name__ == "__main__":
    main()
