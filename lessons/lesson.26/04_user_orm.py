import random
from typing import Sequence

from sqlalchemy import String
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session

from common import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
        unique=True,
    )


CREATED_AS_SQL = """\
CREATE TABLE users
(
    id       INTEGER     NOT NULL,
    username VARCHAR(40) NOT NULL,
    email    VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE (email)
)
"""


def is_lottery_winner(user: User) -> bool:
    # some bool random based on user.username:
    is_winner = random.choice([True, False])
    print("user", user.username, "is winner?", is_winner)
    return is_winner


def save_new_users(session: Session):
    # user = User(
    #     username="bob",
    #     email="bob@ya.ru",
    # )
    # session.add(user)
    users = [
        # User(
        #     username="Nick",
        # ),
        # User(
        #     username="John",
        #     email="john@abc.com",
        # ),
        User(
            username="kyle",
        ),
    ]
    session.add_all(users)
    session.commit()


def generate_emails_for_users(session: Session):
    # val = None
    # val = "asd"
    stmt = (
        update(User)
        .where(
            User.email.is_(None),
            # User.email.isnot(None),
            # User.email == val,
        )
        .values(
            {
                User.email: func.lower(User.username + "@default.org"),
            },
        )
    )
    session.execute(stmt)
    session.commit()


NEW_UPDATE_SQL = """
UPDATE users
SET email=(users.username || '@default.org')
WHERE users.email IS NULL
"""

LOWER_UPDATE_SQL = """
UPDATE users
SET email=lower(users.username || '@default.org')
WHERE users.email IS NULL
"""


def draw_winners(session: Session):
    # users = session.query(User).order_by(User.id)
    stmt = select(User).order_by(User.id)
    users: Sequence[User] = session.scalars(stmt).all()
    for user in users:
        if is_lottery_winner(user):
            user.username = f"{user.username} (WINNER)"

    session.commit()


WINNERS_SQL = """\
UPDATE users
SET username=$1 WHERE users.id = $2
VALUES (
    ('Nick (WINNER)', 2),
    ('John (WINNER)', 3)
)
"""


def main():
    print(Base.metadata.tables)
    print(repr(User.__table__))

    Base.metadata.create_all(bind=engine)
    # user_sam_stmt = select(User).where(User.username == "sam")
    # # user_sam_stmt = select(User).filter_by(user_name="sam")
    # print(user_sam_stmt)
    with Session(engine) as session:
        save_new_users(session)
        generate_emails_for_users(session)
        draw_winners(session)


if __name__ == "__main__":
    main()
