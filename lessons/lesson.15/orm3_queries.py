# import os
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
    sessionmaker,
    scoped_session,
    Session as SessionType,
)

# user = os.getenv("PG_USER")
DB_URL = "postgresql+pg8000://username:passwd!@localhost:5432/blog"
DB_ECHO = True
engine = create_engine(url=DB_URL, echo=DB_ECHO)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(bind=engine, cls=Base)


class User(Base):
    __tablename__ = "users"

    username = Column(String(20), unique=True)
    is_staff = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def promote(self):
        self.is_staff = True

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f"username={self.username!r},"
            f"is_staff={self.is_staff},"
            f"created_at={self.created_at}"
            ")"
        )

    def __repr__(self):
        return str(self)


def create_table():
    sql = """
    CREATE TABLE users (
        id SERIAL NOT NULL, 
        username VARCHAR(20), 
        is_staff BOOLEAN NOT NULL, 
        created_at TIMESTAMP WITHOUT TIME ZONE, 
        PRIMARY KEY (id), 
        UNIQUE (username)
    )
    """
    Base.metadata.create_all()


def query_all_users(session: SessionType) -> list[User]:
    sql = """
    SELECT users.id AS users_id
        , users.username AS users_username
        , users.is_staff AS users_is_staff
        , users.created_at AS users_created_at 
    FROM users
    """
    users = session.query(User).all()
    print("received users:", users)
    return users


def create_user(session: SessionType, username: str) -> User:
    user = User(username=username)
    print("create user", user)

    session.add(user)
    session.commit()

    print("saved user", user)

    return user


def find_user_by_username(session: SessionType, username: str) -> User:
    sql = """
    SELECT users.id AS users_id
        , users.username AS users_username
        , users.is_staff AS users_is_staff
        , users.created_at AS users_created_at 
    FROM users 
    WHERE users.username = %s
    """
    user = session.query(User).filter_by(username=username).one()
    # user = session.query(User).filter_by(username=username).one_or_none()
    # user = session.query(User).filter_by(username=username).first()
    print("found user", user)
    return user


def get_user_by_id(session: SessionType, id: int) -> User:
    user = session.query(User).filter_by(id=id).one()
    print("user", user)
    user = session.get(User, id)
    print("got user", user)
    return user


def find_users_by_username(session: SessionType, name_part: str) -> list[User]:
    q_users = session.query(User)

    q_users_match_username = q_users.filter(
        User.username.like(f"%{name_part}")
    )
    users = q_users_match_username.all()
    print(f"found users for {name_part!r}", users)

    return users


def promote_user(session: SessionType, user: User) -> User:
    sql = """
    UPDATE users 
    SET is_staff=TRUE 
    WHERE users.id = 3
    """
    print("before", user)
    user.promote()
    # user.username = "vasya"
    print("after", user)

    session.commit()

    print("after commit", user)
    return user


def main():
    # create_table()

    session: SessionType = Session()

    # result = session.execute("SELECT 1, 2, now();")
    # print(result)
    # for res in result:
    #     print(res)

    query_all_users(session)
    create_user(session, "jack")
    create_user(session, "nick")
    user_jack = find_user_by_username(session, "jack")
    get_user_by_id(session, 4)
    find_users_by_username(session, "admin")
    find_users_by_username(session, "ck")
    find_users_by_username(session, "ick")

    promote_user(session, user_jack)

    session.close()


if __name__ == '__main__':
    main()
