from pydantic import (
    BaseModel,
    EmailStr,
)


class AuthorBaseSchema(BaseModel):
    name: str
    username: str
    email: EmailStr | None = None


class AuthorCreateSchema(AuthorBaseSchema):
    """
    Create Author
    """


class AuthorReadSchema(AuthorBaseSchema):
    id: int
    promocode: str
