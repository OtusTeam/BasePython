"""
Users CRUD

Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from schemas.user import UserCreateSchema


class UsersCRUD:
    def __init__(self, session: Session):
        self.session = session

    def get(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        return list(self.session.scalars(stmt).all())

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def create(self, user_create: UserCreateSchema) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
