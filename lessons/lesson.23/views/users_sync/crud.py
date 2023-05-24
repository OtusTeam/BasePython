from sqlalchemy.orm import Session

from models import User

from .schemas import UserIn


def get_users(session: Session) -> list[User]:
    return session.query(User).all()


def create_user(session: Session, user_in: UserIn) -> User:
    # user = User(username=user_in.username)
    user = User(**user_in.dict())
    session.add(user)
    session.commit()
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_user_by_token(session: Session, token: str) -> User | None:
    return session.query(User).filter(User.token == token).one_or_none()
