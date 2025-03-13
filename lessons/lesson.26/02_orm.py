from datetime import datetime

from sqlalchemy import (
    create_engine,
    func,
    String,
    select,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    DeclarativeBase,
    Session,
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    # id = Column(Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    full_name: Mapped[str] = mapped_column(
        String(100),
        default="",
        server_default="",
    )
    email: Mapped[str | None] = mapped_column(String(120), unique=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )

    # def add_friend(self, friend: User):
    #     self.friends.append(friend)


def create_users(engine):

    bob = User(
        username="bob",
        email="bob@example.com",
    )
    alice = User(
        username="alice",
    )
    john = User(
        username="john",
        full_name="John Smith",
    )
    with Session(engine) as session:
        session.add(bob)
        session.commit()

        session.add(alice)
        session.add(john)

        session.commit()


def main():
    print(Base.metadata.tables)
    print(repr(Base.metadata.tables["users"]))
    print(repr(User.__table__))

    engine = create_engine(
        # "sqlite:///:memory:",
        "sqlite:///users.db",
        echo=True,
    )
    # print(Base.metadata.tables)
    # metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # create_users(engine)
    # stmt = select(User).order_by(User.id)
    stmt = select(User).order_by(User.username)
    with Session(engine) as session:
        result = session.execute(stmt)
        # print(result.scalars().all())
        users = result.scalars().all()
    for user in users:
        print(user.id, user.username, user.full_name, user.email, user.created_at)


if __name__ == "__main__":
    main()
