import logging
from typing import Annotated

import aiohttp
import httpx
from annotated_types import Gt, Lt
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas.user import UserOut, UserCreate, UsersDataOut
from .dependencies import get_user_by_token, get_session
from . import crud
from schemas.common.pagination import LimitOffsetPaginationSchema

router = APIRouter()

log = logging.getLogger(__name__)


@router.get("/", response_model=UsersDataOut)
async def get_users(
    pagination: LimitOffsetPaginationSchema = Depends(LimitOffsetPaginationSchema),
    session: AsyncSession = Depends(get_session),
):
    users: list[User] = await crud.get_users(
        session=session,
        limit=pagination.limit,
        offset=pagination.offset,
    )
    users_count: int = await crud.get_users_count(session)
    return UsersDataOut(
        data=users,
        meta={
            "pagination": {
                "total_count": users_count,
                **pagination.model_dump(),
            },
        },
    )


@router.get("/all/", response_model=list[UserOut])
async def get_users(
    session: AsyncSession = Depends(get_session),
):
    return await crud.get_users(session=session)


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    return await crud.create_user(
        session=session,
        user_in=user_in,
    )


@router.post(
    "/create-many/",
    response_model=list[UserOut],
    status_code=status.HTTP_201_CREATED,
)
async def create_many_users(
    n_users: Annotated[int, Gt(0), Lt(10_000)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    users: list[User] = await crud.create_many_users(
        session=session,
        n_users=n_users,
    )
    return users


@router.get(
    "/me/",
    response_model=UserOut,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Not Authorized",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Could not validate credentials",
                    },
                },
            },
        },
    },
)
def get_user_me(
    user: Annotated[User, Depends(get_user_by_token)],
):
    return user


@router.get(
    "/{user_id}/",
    response_model=UserOut,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User #0 not found!",
                    },
                },
            },
        },
    },
)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    async with aiohttp.ClientSession() as sess:
        async with sess.get("https://example.com") as response:
            result = await response.text()
    log.info("Response %s", result)

    user: User | None = await crud.get_user(
        session=session,
        user_id=user_id,
    )
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
