"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from schemas import UserCreate
from models import User


class UsersCRUD:
    def __init__(self, session: Session):
        self.session = session

    def get(self) -> list[User]:
        statement = select(User).order_by(User.id)
        return list(self.session.scalars(statement).all())

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def get_by_token(self, token: str) -> User | None:
        statement = select(User).where(User.token == token)
        return self.session.execute(statement).scalar_one_or_none()

    def create(self, user_in: UserCreate) -> User:
        user = User(
            **user_in.model_dump(),
        )
        self.session.add(user)
        self.session.commit()
        return user
