"""
CRUD functions for users

Create
Read
Update
Delete
"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from .schemas import UserCreate, UserUpdate


class UsersStorage:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_user(self, user_in: UserCreate) -> User:
        user = User(**user_in.model_dump())
        self.session.add(user)
        self.session.commit()
        return user

    def get_users(self) -> list[User]:
        result = self.session.scalars(select(User)).all()
        return list(result)

    def get_user(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def get_user_by_token(self, token: str) -> User | None:
        stmt = select(User).where(User.token == token)
        # return self.session.scalars(stmt).one_or_none()
        return self.session.scalar(stmt)

    def delete_user(self, user: User) -> None:
        # stmt = delete(User).where(User.id == user_id)
        # self.session.execute(stmt)
        self.session.delete(user)
        self.session.commit()

    def update_user(self, user: User, user_in: UserUpdate):
        for name, value in user_in.model_dump(exclude_unset=True).items():
            setattr(user, name, value)
        self.session.commit()
        return user
