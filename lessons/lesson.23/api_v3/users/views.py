import asyncio

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.db_async import scoped_session_dependency as session_dependency

# from models.db_async import session_dependency
from . import crud
from .dependencies import get_user_by_token
from .schemas import UserIn, UserOut

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[UserOut])
async def get_users(
    session: AsyncSession = Depends(session_dependency),
) -> list[UserOut]:
    return await crud.get_users(session)


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "model": UserOut,
        }
    },
)
async def create_user(
    user_in: UserIn,
    session: AsyncSession = Depends(session_dependency),
):
    return await crud.create_user(session=session, user_in=user_in)


@router.post("/create-many/")
async def create_many(
    n_users: int,
    session: AsyncSession = Depends(session_dependency),
):
    return await crud.create_many_users(session=session, n_users=n_users)


@router.get("/me/", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return user


@router.get(
    "/{user_id}/",
    response_model=UserOut,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Not found"},
    },
)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(session_dependency),
):
    await asyncio.sleep(0.5)
    user: User = await crud.get_user_by_id(session=session, user_id=user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found!",
    )
