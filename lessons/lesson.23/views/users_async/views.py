from asyncio import sleep

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.db_async import get_session
from .schemas import UserOut, UserIn
from . import crud
from .dependencies import get_user_by_auth_token

router = APIRouter(
    tags=["Users Async"],
)


@router.get(
    "/",
    response_model=list[UserOut],
)
async def get_users(session: AsyncSession = Depends(get_session)):
    return await crud.get_users(session=session)


@router.post(
    "/",
    response_model=UserOut,
    description="Creates a user",
)
async def create_user(
    user_in: UserIn,
    session: AsyncSession = Depends(get_session),
):
    return await crud.create_user(
        session=session,
        user_in=user_in,
    )


@router.get("/me/", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_auth_token)):
    return user


@router.get(
    "/{user_id}/",
    response_model=UserOut,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "string",
                                "example": "User #0 not found!",
                            },
                        },
                    }
                }
            },
        },
    },
)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(get_session),
) -> User:
    await sleep(0.5)
    user: User | None = await crud.get_user_by_id(session=session, user_id=user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found!",
    )
