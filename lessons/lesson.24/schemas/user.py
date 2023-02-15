from pydantic import BaseModel, constr


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=32)


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
