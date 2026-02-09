from pydantic import (
    BaseModel,
    EmailStr,
    constr,
)


class UserBase(BaseModel):
    username: str
    email: str | None
    full_name: str


class UserCreate(UserBase):
    username: constr(min_length=3, max_length=32)
    email: EmailStr | None = None
    full_name: constr(max_length=1000)


class UserRead(UserBase):
    id: int
