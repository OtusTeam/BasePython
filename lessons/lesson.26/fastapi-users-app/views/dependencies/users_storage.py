from fastapi import Depends
from sqlalchemy.orm import Session

from views.users.crud import UsersStorage
from .db_session import get_session


def get_users_storage(
    session: Session = Depends(get_session),
) -> UsersStorage:
    return UsersStorage(session=session)
