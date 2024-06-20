from collections.abc import Sequence

from sqlalchemy import desc
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy import update
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email!r}"
            ")"
        )


def create_tables():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)

    session.commit()

    print("user created:", user)
    return user


def create_users(
    session: Session,
    *usernames: str,
) -> Sequence[User]:
    users = [
        User(username=username)
        for username in usernames
    ]
    session.add_all(users)
    print("prepared users:", users)

    session.commit()

    print("saved users:", users)
    return users


def fetch_all_users(session: Session) -> Sequence[User]:
    # stmt = select(User).order_by(User.id)
    stmt = select(User).order_by(desc(User.username))
    # result = session.execute(stmt)
    # users = result.scalars().all()
    users = session.scalars(stmt).all()
    print("users:", users)
    return users


def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    # result = session.execute(stmt)
    # user = result.scalars().one_or_none()
    user: User | None = session.scalars(stmt).one_or_none()
    print("user for username", repr(username), "result:", user)
    return user


SQL = """
UPDATE users 
SET email=concat(
    lower(users.username), 
    '@ya.ru'::VARCHAR
)
WHERE users.email IS NULL 
    AND length(users.username) < 5::INTEGER;
"""


def set_emails_for_null_email_users_with_username_limit(
    session: Session,
    username_size_limit: int,
    domain: str,
):
    """

    :param session:
    :param username_size_limit:
    :param domain: example: '@ya.ru'
    :return:
    """

    new_email = (
        func.concat(
            func.lower(User.username),
            domain.lower(),
        )
    )
    stmt = (
        update(User)
        .where(
            # empty email
            User.email.is_(None),
            # username len limit
            func.length(User.username) < username_size_limit,
        )
        .values(
            {
                User.email: new_email,
            }
        )
    )

    session.execute(stmt)
    session.commit()


def main():
    create_tables()
    with Session(engine) as session:
        # create_user(session, username="admin", email="admin@admin.com")
        # create_user(session, username="john", email=None)
        # create_users(session, "nick", "bob", "alice")
        # fetch_all_users(session)
        # fetch_user_by_username(session, "bob")
        # fetch_user_by_username(session, "jack")
        set_emails_for_null_email_users_with_username_limit(
            session,
            username_size_limit=5,
            domain="@ya.ru",
        )


if __name__ == "__main__":
    main()
