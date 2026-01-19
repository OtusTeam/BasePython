from sqlalchemy import (
    String,
    Text,
    create_engine,
    select,
    func,
    ForeignKey,
    event,
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
    relationship,
    joinedload,
)


import config

engine = create_engine(
    url=config.SQLA_SQLITE_DB_URL,
    echo=config.SQLA_DB_ECHO,
)


if "sqlite" in config.SQLA_SQLITE_DB_URL:
    # only for sqlite!
    @event.listens_for(engine, "connect")
    def enable_sqlite_fks(dbapi_connection, connection_record):
        # Add an event listener to enable foreign keys for all new connections
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(String(150), unique=True)
    full_name: Mapped[str] = mapped_column(String(100), server_default="")

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

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


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), server_default="")
    text: Mapped[str] = mapped_column(Text, server_default="")
    user_id: Mapped[int] = mapped_column(
        # ForeignKey("users.id"),
        ForeignKey(User.id),
    )
    user: Mapped[User] = relationship(
        back_populates="posts",
    )

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id!r}"
            f", title={self.title!r}"
            f", text={self.text!r}"
            f", user_id={self.user_id!r}"
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
    user_alice = User(
        username="alice",
    )
    user_bob = User(
        username="bob",
        email="bob@example.com",
    )

    # users = [
    #     user_john,
    #     user_alice,
    #     user_bob,
    # ]

    post1 = Post(
        title="post by john - j(1)",
        user=user_john,
    )
    # post1.user = user_john

    post2 = Post(
        title="post by alice - a(1)",
        user=user_alice,
    )
    # post2.user = user_alice

    post3 = Post(
        title="post by alice - a(2)",
        user=user_alice,
        # user_id=999,
    )
    # post3.user = user_alice

    users = [
        user_john,
        user_alice,
        user_bob,
    ]
    posts = [post1, post2, post3]

    with Session(engine) as session:
        session.add_all(users)
        session.add_all(posts)
        session.commit()


def fetch_values() -> None:
    statement = (
        select(Post)
        .options(
            joinedload(Post.user),
        )
        .order_by(Post.id)
    )

    with Session(engine) as session:
        posts = session.scalars(statement).all()

    for post in posts:
        print("- post", post)
        print("     by", post.user)


def main() -> None:
    # create_tables()
    # insert_values()
    fetch_values()


if __name__ == "__main__":
    main()
