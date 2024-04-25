from fastapi import Depends
from sqlalchemy.orm import Session

from api_v1.views.users.crud import UsersStorage
from views.dependencies.db_session import get_session


def get_users_storage(
    session: Session = Depends(get_session),
) -> UsersStorage:
    return UsersStorage(session=session)
