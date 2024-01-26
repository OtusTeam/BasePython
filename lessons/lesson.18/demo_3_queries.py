from typing import Sequence

from sqlalchemy import Column
from sqlalchemy import select
from sqlalchemy import or_
from sqlalchemy import and_
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

from db import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"User("
            f"id={self.id},"
            f" username={self.username!r},"
            f" email={self.email!r})"
        )


def create_tables():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    session.add(user)
    session.commit()

    print("saved user")
    print("user info:", user)
    # session.refresh(user)

    return user


def create_users(
    session: Session,
    *usernames: str,
) -> list[User]:
    users = [
        # create new user
        User(username=username)
        # for each username
        for username in usernames
    ]
    session.add_all(users)
    session.commit()
    print("saved users:", users)
    return users


def get_user_by_primary_key(
    session: Session,
    pk: int,
) -> User | None:
    # user = session.get(User, pk)
    user = session.get(User, pk)
    # session.refresh(user)
    print("user for pk", pk, "result:", user)
    return user


def find_user_by_pk(
    session: Session,
    pk: int,
) -> User:
    stmt = select(User).where(
        User.id == pk,
        # User.id > 10,
    )
    # result = session.execute(stmt)
    # user = result.scalar()
    # user = session.scalar(stmt)
    result = session.execute(stmt)
    # user: User | None = result.scalar_one_or_none()
    # user: User = result.scalar_one()
    # user: User = result.scalars().first()
    user: User = result.scalar_one()
    print(user)
    return user


def find_user_by_username(
    session: Session,
    username: str,
) -> User | None:
    stmt = select(User).where(User.username == username)
    # user: User | None = session.scalar(stmt)
    user: User | None = session.scalars(stmt).one_or_none()
    print("user username", username, user)
    return user


def search_users(
    session: Session,
) -> Sequence[User]:
    no_email_and_a_in_username_condition = and_(
        User.email.isnot(None),
        User.username.ilike("%a%"),
    )
    stmt = (
        select(User)
        .where(
            or_(
                User.username.ilike("%e"),
                no_email_and_a_in_username_condition,
            )
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()

    for user in users:
        print(user)

    # print(list(users))
    return users


def main():
    create_tables()

    with Session(engine, expire_on_commit=False) as session:
        create_user(session, "john")
        create_user(session, "sam", "sam@example.com")

        create_users(
            session,
            "bob",
            "alice",
            "kate",
            "jack",
        )

        get_user_by_primary_key(session, 0)
        get_user_by_primary_key(session, 1)
        get_user_by_primary_key(session, 3)
        get_user_by_primary_key(session, 10)
        find_user_by_pk(session, 1)
        # find_user_by_pk(session, 0)
        find_user_by_username(session, "bob")
        find_user_by_username(session, "sam")
        find_user_by_username(session, "qwerty")
        search_users(session)


if __name__ == "__main__":
    main()
