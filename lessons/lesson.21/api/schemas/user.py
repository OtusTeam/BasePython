from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=32) = Field(..., example="john")

    # class Config:
    #     orm_mode = False


class UserOut(UserBase):
    id: int = Field(..., example=123)

    class Config:
        orm_mode = True


class UserIn(UserBase):
    """
    Create user
    """
