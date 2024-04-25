from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v2.views.users.crud import UsersStorage
from views.dependencies.db_session import get_async_session


def get_users_storage(
    session: AsyncSession = Depends(get_async_session),
) -> UsersStorage:
    return UsersStorage(session=session)
