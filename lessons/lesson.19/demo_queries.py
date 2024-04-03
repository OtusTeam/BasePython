from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import update
from sqlalchemy import func

from sqlalchemy.orm import DeclarativeBase, Session

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
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email!r}"
            f")"
        )


def create_tables():
    Base.metadata.create_all(bind=engine)


def example_calc(session: Session):
    result = session.execute(select(1))

    # print(result.all())
    # print(result.one())
    print(result.scalar())

    # SELECT 1 + 2;
    result = session.execute(select(text("1 + 2")))
    print(result.scalar())


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print("created user:", user)
    return user


def create_users(
    session: Session,
    *usernames: str,
) -> list[User]:
    users = [
        User(username=username)
        for username in usernames
    ]
    session.add_all(users)
    print("prepared users:", users)
    session.commit()

    print("created users:", users)
    return users


def fetch_all_users(session: Session) -> list[User]:
    stmt = select(User).order_by(User.id)
    users = session.scalars(stmt).all()
    # result = session.execute(stmt)
    # users = result.scalars().all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list


def fetch_user_by_id(session: Session, user_id: int) -> User | None:
    # stmt = select(User).where(User.id == user_id)
    # user = session.scalar(stmt)
    user = session.get(User, user_id)
    print("user:", user)
    return user


def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user = session.scalar(stmt)
    print("user:", user)
    return user


def update_users_emails(
    session: Session,
    username_len: int,
    email_domain: str,
):
    stmt = update(User).where(
        User.email.is_(None),
        func.length(User.username) > username_len,
    ).values(
        {
            User.email: func.concat(func.lower(User.username), email_domain.lower()),
            # User.username: "aqwe"
        }
    )
    session.execute(stmt)
    # print(result.all())
    session.commit()


def fetch_users_for_domain(session: Session, domain: str) -> list[User]:
    stmt = select(User).where(
        User.email.ilike(f"%{domain.lower()}")
    )
    users = session.scalars(stmt).all()
    print(f"users for domain {domain}:", users)
    return users


def main():
    # Base.metadata.drop_all(bind=engine)
    create_tables()

    with Session(engine) as session:
        # example_calc(session)
        # create_user(session, "john")
        # create_user(session, "sam", email="sam@example.com")
        # create_users(
        #     session,
        #     "bob",
        #     "alice",
        #     "nick",
        # )
        fetch_all_users(session)
        # fetch_user_by_id(session, 1)
        # fetch_user_by_id(session, 0)
        # fetch_user_by_id(session, 1)
        # fetch_user_by_username(session, "john")
        # fetch_user_by_username(session, "bob")
        # fetch_user_by_username(session, "abc")
        # fetch_user_by_username(session, "qwe")

        update_users_emails(session, 3, "@ya.ru")
        update_users_emails(session, 1, "@example.com")

        fetch_all_users(session)

        fetch_users_for_domain(session, domain="@ya.ru")
        fetch_users_for_domain(session, domain="@example.com")
        fetch_users_for_domain(session, domain="@qwerty.abc")


if __name__ == "__main__":
    main()
