from datetime import datetime, timedelta
from typing import List, Optional
from pprint import pprint

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func,
    or_,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

engine = create_engine("sqlite:///example-db-04.sqlite", echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"
    #
    # def __init__(self, username, is_staff):
    #     self.username = username
    #     self.is_staff = is_staff

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username!r}, is_staff={self.is_staff}, "
            f"created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)


def create_admin():
    session = Session()

    username = "admin"
    admin = User(username=username, is_staff=True)
    print("new admin:", admin)

    session.add(admin)

    try:
        session.commit()
    except IntegrityError as e:
        print("oops could not save user", admin, e)
        session.rollback()
    else:
        print("created admin:", admin)

    session.close()


def create_and_edit_user():
    session = Session()

    username = "jonh"
    user = User(username=username)
    print("new user:", user)

    session.add(user)
    session.commit()

    print("created user:", user)
    print("oops! update username!")
    user.username = "john"
    session.commit()
    print("updated user:", user)

    session.close()


def get_users():
    session = Session()

    users: List[User] = session.query(User).all()
    print("users:")
    pprint(users)

    session.close()


def get_admin():
    session = Session()

    user: User = session.query(User).filter_by(username="admin").one()
    # user: Optional[User] = session.query(User).filter_by(username="admin").one_or_none()
    print(user)

    session.close()


def get_user():
    session = Session()

    # user: User = session.query(User).filter_by(username="admin").one()
    user: Optional[User] = session.query(User).filter_by(username="sam").one_or_none()
    # if user is None
    if not user:
        print("could not find user!")
    print(user)

    session.close()


def get_users_filtered():
    session = Session()

    users: List[User] = (
        session
        .query(User)
        .filter(User.id > 2)
        .all()
    )
    pprint(users)

    session.close()


def get_recent_users():
    session = Session()

    now = datetime.utcnow()

    recent_time = now - timedelta(minutes=15)
    print("recent_time")
    print(recent_time)
    users: List[User] = (
        session
        .query(User)
        .filter_by(is_staff=False)
        .filter(
            User.created_at > recent_time,
        )
        .all()
    )
    print("recent users")
    pprint(users)

    session.close()


def get_some_recent_users():
    session = Session()

    now = datetime.utcnow()

    recent_time = now - timedelta(minutes=20)
    print("recent_time")
    print(recent_time)
    users: List[User] = (
        session
        .query(User)
        # .filter_by(is_staff=False)
        .filter(
            or_(
                User.created_at > recent_time,
                # User.is_staff == True,
                User.is_staff.is_(True),
            ),

        )
        .all()
    )
    print("some recent users")
    pprint(users)

    session.close()


def get_user_by_pk():
    session = Session()

    u1 = session.query(User).get(1)
    print("u1", u1)

    session.close()


def main():
    Base.metadata.create_all()
    create_admin()
    create_and_edit_user()
    get_users()
    get_admin()
    get_user()
    get_users_filtered()
    get_recent_users()
    get_some_recent_users()
    get_user_by_pk()


if __name__ == "__main__":
    main()
