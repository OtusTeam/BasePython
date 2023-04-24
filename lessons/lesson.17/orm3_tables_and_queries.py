from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    func,
    false,
)
from sqlalchemy.orm import (
    declarative_base,
    Session,
)

# DB_URL = "postgresql+pg8000"
DB_URL = "postgresql+psycopg2://username:passwd@0.0.0.0:5432/blog"

DB_ECHO = False
# DB_ECHO = True


engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO,
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(180), unique=True)
    archived = Column(
        Boolean,
        default=False,
        server_default=false(),
        nullable=False,
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, created_at={self.created_at})"

    def __repr__(self):
        return str(self)


def create_user(session: Session, username: str) -> User:
    user = User(username=username)
    print("user", user)
    session.add(user)
    session.commit()
    print("saved user", user)
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    user = session.get(User, user_id)
    print("user by id", user_id, "value:", user)
    return user


def get_all_users(session: Session) -> list[User]:
    users = session.query(User).all()
    print("users:", users)
    return users


def get_user_by_username(session: Session, username: str) -> User | None:
    user: User | None = (
        session.query(User)
        # search by username
        .filter_by(username=username)
        # find one or none
        .one_or_none()
    )
    print("found user", user)
    return user


def get_users_by_username_match(session: Session, username_part: str) -> list[User]:
    users: list[User] = (
        session.query(User)
        # .filter(User.id.in_([1, 2, 3, 5, 7]))
        # .filter(User.username == username_part)
        .filter(
            # one
            User.username.ilike(f"%{username_part}%"),
            # two
            # User.archived == False,
            User.archived.is_(False),
            # User.archived.isnot(True),
        )
        # get all of them
        .all()
    )
    print(f"found users for part {username_part!r}:", users)
    return users


def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        create_user(session, username="john")
        create_user(session, username="sam")
        create_user(session, username="bob")

        get_user_by_id(session, 1)
        get_user_by_id(session, 4)

        get_all_users(session)
        get_user_by_username(session, "john")
        get_user_by_username(session, "bob")
        get_users_by_username_match(session, "o")


if __name__ == "__main__":
    main()
