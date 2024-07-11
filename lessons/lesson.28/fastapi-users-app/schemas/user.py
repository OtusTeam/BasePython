from pydantic import (
    BaseModel,
    EmailStr,
    Field,
)

UserIdType = int


class UserBase(BaseModel):
    username: str
    email: EmailStr | None = None


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: UserIdType = Field(
        ...,
        description="The id of the user",
        example=42,
    )
