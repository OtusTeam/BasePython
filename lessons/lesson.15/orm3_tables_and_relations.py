from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    false,
    func,
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session as SessionType,
)

DB_URL = "postgresql+psycopg2://username:passwd!@0.0.0.0:5432/blog"
DB_ECHO = True
# DB_ECHO = False

engine = create_engine(url=DB_URL, echo=DB_ECHO)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"
    # __table_args__ = {
    #
    # }

    id = Column(Integer, primary_key=True)
    # 1
    # id = Column(Integer, primary_key=True, autoincrement=False)
    # 2
    # left_id = Column(Integer, primary_key=True)
    # right_id = Column(Integer, primary_key=True)
    # 3
    # id = Column(String, primary_key=True)

    username = Column(String(20), unique=True)
    archived = Column(
        Boolean,
        default=False,
        server_default=false(),
        nullable=False,
    )
    # archived = Column(Boolean, default=False, server_default="FALSE")
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)


def create_user(session: SessionType, username: str) -> User:
    user = User(username=username)

    session.add(user)

    print(user)
    session.commit()
    print(user)

    return user


def get_users(session: SessionType) -> list[User]:
    users = session.query(User).all()
    print(users)
    return users


def get_user_by_id(session: SessionType, user_id: int) -> User | None:
    # user = session.query(User).filter_by(id=user_id).one_or_none()
    # user = session.query(User).filter(User.id == user_id).one_or_none()
    # user = session.query(User).filter_by(id=user_id).one()
    user = session.get(User, user_id)
    print(user)
    return user


def get_user_by_ids(session: SessionType, *user_ids: int) -> list[User]:
    users = session.query(User).filter(
        User.id.in_(user_ids),
    ).all()
    print(users)
    return users


def get_user_by_username(session: SessionType, username: str) -> User | None:
    user = session.query(User).filter(User.username == username).one_or_none()
    print(user)
    return user


def get_user_by_username_match(
    session: SessionType,
    username_part: str,
) -> User | None:
    users = session.query(User).filter(
        User.username.ilike(f"%{username_part}%"),
    ).all()
    print(users)
    return users


def main():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    session: SessionType = Session()

    create_user(session, "john")
    create_user(session, "sam")
    user = create_user(session, "nick")
    user.archived = True
    session.commit()

    get_users(session)
    get_user_by_id(session, 1)
    get_user_by_id(session, 2)
    get_user_by_id(session, 3)
    get_user_by_username(session, "john")
    get_user_by_ids(session, 0, 2, 1, 3)
    get_user_by_username_match(session, "n")

    session.close()


if __name__ == "__main__":
    main()

