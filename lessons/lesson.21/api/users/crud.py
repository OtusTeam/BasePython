"""
Create
Read
Update
Delete
"""
import requests
from sqlalchemy.orm import Session

from models import User
from api.schemas.user import UserIn


# Get
def get_users(session: Session) -> list[User]:
    return session.query(User).order_by(User.id).all()


# Get (details)
def get_user_by_id(session: Session, user_id: int) -> User | None:
    response = requests.get("https://httpbin.org/get")
    data = response.json()
    return session.get(User, user_id)


def get_user_by_token(session: Session, token: str) -> User | None:
    return session.query(User).filter_by(token=token).one_or_none()


# CREATE
def create_user(session: Session, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(user)
    session.commit()
    return user


# Delete
# def delete_user(session: Session, user: User) -> None:
#     session.delete(user)

def delete_user(session: Session, user_id: int) -> None:
    session.query(User).filter(User.id == user_id).delete()
    session.commit()
