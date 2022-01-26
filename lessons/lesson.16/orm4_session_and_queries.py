from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import (
    declarative_base,
    scoped_session,
    sessionmaker,
)

DB_URL = "sqlite:///example-04.db"
engine = create_engine(DB_URL, echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# session = session_factory()
# session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self.id}, " \
               f"username={self.username!r}, " \
               f"is_staff={self.is_staff}, " \
               f"created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    """
    :param username:
    :return:
    """
    session = Session()

    user = User(username=username)
    print("created", user)

    session.add(user)
    session.commit()

    print("saved", user)

    session.close()
    return user


def get_all_users() -> list[User]:
    session = Session()

    users = session.query(User).all()

    session.close()
    return users


def get_user(username: str) -> User:
    """
    :param username:
    :return:
    """
    session = Session()

    user = session.query(User).filter_by(username=username).one()
    # user = session.query(User).filter_by(username=username).one_or_none()
    # user = session.query(User).filter_by(username=username).first()

    session.close()
    return user


def find_user_by_str(name_part: str) -> list[User]:
    session = Session()

    query = session.query(User).filter(
        User.username.like(f"%{name_part}%"),
    )
    users = query.all()

    session.close()
    return users


def user_creation():
    """
    :return:
    """

    create_user("john")
    """
    INSERT INTO users (username, is_staff, created_at) VALUES (?, ?, ?)
    ('john', 0, '2022-01-26 17:54:09.686618');

    SELECT users.id AS users_id
         , users.username AS users_username
         , users.is_staff AS users_is_staff
         , users.created_at AS users_created_at
    FROM users
    WHERE users.id = ?
    (1,)
    """

    create_user("sam")
    create_user("samanta")


def user_fetching():
    users = get_all_users()
    print(users)
    # user = get_user("samuel")
    user = get_user("sam")
    print(user)

    users = find_user_by_str("oh")
    print(users)


def user_updating():
    """
    UPDATE users SET is_staff=1 WHERE users.id = 2
    :return:
    """
    session = Session()

    user: User = session.query(User).filter_by(username="sam").one()
    print("before:", user)
    user.is_staff = True

    session.commit()
    print("after:", user)

    session.close()


def main():
    # Base.metadata.create_all()
    # """
    # CREATE TABLE users (
    #     id INTEGER NOT NULL,
    #     username VARCHAR(32),
    #     is_staff BOOLEAN NOT NULL,
    #     created_at DATETIME,
    #     PRIMARY KEY (id),
    #     UNIQUE (username)
    # )
    # """
    # user_creation()
    # user_fetching()
    user_updating()


if __name__ == "__main__":
    main()
