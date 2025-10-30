from fastapi_users import schemas
from pydantic import BaseModel

from core.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserRegisteredNotification(BaseModel):
    user: UserRead
    ts: int
