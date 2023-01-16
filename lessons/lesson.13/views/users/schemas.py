from pydantic import BaseModel, constr


class UserBase(BaseModel):
    username: str


class UserIn(UserBase):
    pass


class User(UserBase):
    id: int

