from typing import Sequence

from sqlalchemy import select
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy import update
# from sqlalchemy.engine import Result
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

from config import engine


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
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username!r}, email={self.email!r})"
        )


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    print(user)
    session.add(user)
    session.commit()
    print("saved user")
    print("user details:", user)
    return user


def create_users(
    session: Session,
    *usernames: str,
) -> list[User]:
    users = [User(username=username) for username in usernames]
    session.add_all(users)
    session.commit()
    print("saved users:", users)
    return users


def spameggs(foo, bar):
    """

    :param foo: needs X
    :param bar: needs Y
    :return:
    """


def get_user_by_id(
    session: Session,
    user_id: int,
) -> User | None:
    """
    From cache

    :param session:
    :param user_id:
    :return:
    """
    user = session.get(User, user_id)
    print(user)
    # if user is None:
    #     raise ...
    return user


def find_user_by_id(
    session: Session,
    user_id: int,
) -> User | None:
    stmt = select(User).where(User.id == user_id)
    # result: Result = session.execute(stmt)
    # user = result.scalar_one_or_none()
    user = session.scalar(stmt)
    if user is None:
        print("no user by id", user_id)
    else:
        print("found user", user)

    return user


def find_user_by_username(
    session: Session,
    username: str,
) -> User | None:
    # stmt = select(User).where(User.username == username)
    stmt = select(User).where(User.username.ilike(username))
    # stmt = select(User).where(func.lower(User.username) == func.lower(username))
    # result: Result = session.execute(stmt)
    # user = result.scalar_one_or_none()
    user = session.scalar(stmt)
    if user is None:
        print("no user by username", username)
    else:
        print("found user", user)

    return user


def demo_update_users(session: Session):
    fltr_u_w_o = User.username.ilike("%o%")
    stmt_users_w_o = select(User).where(fltr_u_w_o)
    users_w_o = session.scalars(stmt_users_w_o).all()
    print(users_w_o)
    upd_stmt = (
        update(User)
        .where(fltr_u_w_o)
        .values(
            {
                User.email: func.concat(User.username, "@ya.ru"),
                # User.email: "abc",
            }
        )
    )
    session.execute(upd_stmt)
    session.commit()
    users_w_o = session.scalars(stmt_users_w_o).all()
    print(users_w_o)


def find_users(
    session: Session,
) -> Sequence[User]:
    stmt = (
        select(User)
        .where(
            # or_(
            and_(
                User.email.isnot(None),
                User.username.ilike("%n%"),
            ),
        )
        .order_by(User.id)
    )
    users = session.scalars(stmt).all()
    print(users)
    return users


def main():
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        # create_user(session, "john")
        # create_user(session, "sam")
        # create_user(session, "bob")
        # create_user(session, "nick")
        # create_users(session, "sam", "bob", "nick")
        # get_user_by_id(session, 1)
        # get_user_by_id(session, 2)
        # get_user_by_id(session, 1)
        # find_user_by_id(session, 1)
        # find_user_by_id(session, 2)
        # find_user_by_id(session, 5)
        # find_user_by_username(session, "qwerty")
        # find_user_by_username(session, "bob")
        # find_user_by_username(session, "Nick")
        # find_user(session)
        # demo_update_users(session)
        find_users(session)


if __name__ == "__main__":
    main()
