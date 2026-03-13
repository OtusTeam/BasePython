from sqlalchemy import (
    create_engine,
    String,
    select,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
)

import config


engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        # autoincrement=True,
    )
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        String(150),
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        String(100),
        default="",
        server_default="",
    )

    def greet(self) -> str:
        return f"Hello, {self.username}!"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", full_name={self.full_name!r}"
            ")"
        )

    def __repr__(self) -> str:
        return str(self)


def insert_values() -> None:
    user_john = User(
        username="john",
        email="john@example.com",
        full_name="Johnathan",
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


def fetch_values() -> None:
    """"""

    """
    SELECT users.id
         , users.username
         , users.email
         , users.full_name 
    FROM users 
    WHERE users.email IS NOT NULL 
    ORDER BY users.username DESC
    """
    stmt = (
        select(User)
        .where(
            User.email.isnot(None),
        )
        .order_by(User.username.desc())
    )
    with Session(engine) as session:
        result = session.execute(stmt)
        # print(result)
        # print(result.scalars().all())
        users: list[User] = result.scalars().all()

    for user in users:
        print(user)
        print(user.greet())


def main() -> None:
    # print("Base.metadata.tables:", Base.metadata.tables)
    # print({"users": User.__table__})
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    #
    # insert_values()
    fetch_values()


if __name__ == "__main__":
    main()
