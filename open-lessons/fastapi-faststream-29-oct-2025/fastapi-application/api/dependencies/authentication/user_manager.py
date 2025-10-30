from typing import Annotated, TYPE_CHECKING

from fastapi import Depends, BackgroundTasks

from core.authentication.user_manager import UserManager

from .users import get_users_db

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_user_manager(
    users_db: Annotated[
        "SQLAlchemyUserDatabase",
        Depends(get_users_db),
    ],
    background_tasks: BackgroundTasks,
):
    yield UserManager(
        users_db,
        background_tasks=background_tasks,
    )
