from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.db_async import session_dependency
from views.api.schemas import UserSchema, UserCreateSchema
from . import crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserSchema])
async def get_users(
    session: AsyncSession = Depends(session_dependency)
) -> list[User]:
    return await crud.get_users(session=session)


@router.get("/{user_id}/", response_model=UserSchema)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(session_dependency)
) -> User:
    user: User | None = await crud.get_user_by_id(
        session=session,
        user_id=user_id,
    )
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="user_not_found",
    )


@router.post("/", response_model=UserSchema)
async def create_user(
    user_create: UserCreateSchema,
    session: AsyncSession = Depends(session_dependency),
):
    return await crud.create_user(
        session=session,
        user_create=user_create,
    )


@router.post("/create-many/", response_model=list[UserSchema])
async def create_many_users(
    n_users: int = Query(title="Number of users to create"),
    session: AsyncSession = Depends(session_dependency),
) -> list[User]:
    users: list[User] = await crud.create_many_users(
        session=session,
        n_users=n_users,
    )
    return users
