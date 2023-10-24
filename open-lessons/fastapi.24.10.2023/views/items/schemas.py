from pydantic import BaseModel, Field, EmailStr


class NewItemModel(BaseModel):
    # username: constr(min_length=3)
    username: str = Field(min_length=3)
    email: EmailStr
