"""
Create
Read
Update
Delete
"""

from sqlalchemy import delete
from sqlalchemy.orm import Session

from models import User
from schemas.user import UserIn


def get_users(session: Session) -> list[User]:
    return session.query(User).order_by(User.id).all()


def create_user(session: Session, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(user)
    session.commit()
    print("new user", user)
    return user


def get_user(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_user_by_token(session: Session, token: str) -> User | None:
    return session.query(User).filter_by(token=token).one_or_none()


def delete_user(session: Session, user_id: int) -> None:
    session.execute(delete(User).where(User.id == user_id))
    session.commit()
