from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str | None
    full_name: str


class UserRead(UserBase):
    id: int
