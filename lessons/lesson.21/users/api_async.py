from fastapi import APIRouter, HTTPException, Depends
from starlette.status import HTTP_404_NOT_FOUND
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from . import crud_async as crud
from .dependencies import get_db_async, get_user_by_auth_token_async
from .schemas import UserIn, UserOut

router = APIRouter(tags=["Users Async"])


@router.get("", response_model=list[UserOut])
async def list_users(
    session: AsyncSession = Depends(get_db_async),
) -> list[User]:
    return await crud.list_users(session)


@router.post("", response_model=UserOut)
async def create_user(
    user_in: UserIn,
    session: AsyncSession = Depends(get_db_async),
) -> User:
    return await crud.create_user(session, user_in)


@router.get("/me", response_model=UserOut)
async def get_me(user: User = Depends(get_user_by_auth_token_async)):
    return user


@router.get(
    "/{user_id}",
    response_model=UserOut,
    responses={
        HTTP_404_NOT_FOUND: {
            "description": "user not found",
            "content": {
                "application/json": {
                    "schema": {
                        "title": "Not Found",
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "string",
                                "example": "user #0 not found",
                            },
                        },
                    },
                },
            },
        },
    },
)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(get_db_async),
) -> User:
    user = await crud.get_user(session, user_id)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} not found!",
    )
