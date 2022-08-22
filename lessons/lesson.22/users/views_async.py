
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession as Session

from models import User
from models.db_async import get_session_async as get_session
from .schemas import UserIn, UserOut
from . import crud_async as crud
from .dependencies_async import get_user_by_token

router = APIRouter(prefix="/users", tags=["Users Async"])


@router.get("", response_model=list[UserOut])
async def list_users(
    session: Session = Depends(get_session),
) -> list[User]:
    return await crud.list_users(session)


@router.post("", response_model=UserOut)
async def create_user(
    user_in: UserIn,
    session: Session = Depends(get_session),
) -> User:
    return await crud.create_user(session, user_in=user_in)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return user


@router.get("/{user_id}", response_model=UserOut)
async def get_user(
    user_id: int,
    session: Session = Depends(get_session),
) -> User:
    user = await crud.get_user_by_id(session, user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} not found!",
    )
