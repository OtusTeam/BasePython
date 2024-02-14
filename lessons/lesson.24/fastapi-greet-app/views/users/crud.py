"""
Create
Read
Update
Delete
"""

from sqlalchemy import select, func, text
from sqlalchemy.orm import Session

from models import User
from .schemas import UserCreate


def create_user(
    session: Session,
    user_in: UserCreate,
) -> User:
    user: User = User(
        **user_in.model_dump(),
    )
    session.add(user)
    session.commit()
    return user


def get_users(
    session: Session,
    limit: int | None = None,
    offset: int | None = None,
) -> list[User]:
    # statement:
    stmt = select(User).order_by(User.id)
    if limit is not None:
        stmt = stmt.limit(limit)
    if offset is not None:
        stmt = stmt.offset(offset)
    return list(
        # session shortcut
        session.scalars(stmt).all()
    )


def get_users_count(session: Session, stmt=None) -> int:
    if stmt is None:
        stmt = select(User.id)
    return session.scalar(
        select(
            func.count(
                text("*"),
            ),
        ).select_from(
            stmt.subquery(),
        )
    )


def get_user(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_user_by_token(session: Session, token: str) -> User | None:
    stmt = select(User).where(User.token == token)
    return session.scalar(stmt)
