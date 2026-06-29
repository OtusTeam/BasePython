from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User


class Crud:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_users(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        users = self.session.scalars(stmt)
        return list(users.all())

    def get_user(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)
