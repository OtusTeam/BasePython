from typing import Annotated

from pydantic import BaseModel, Field
from annotated_types import MinLen


ProductIdType = int


class ProductBaseSchema(BaseModel):
    name: str
    price: int


class ProductCreateSchema(ProductBaseSchema):
    """
    Create new product w/ this data
    """

    name: Annotated[str, MinLen(3)]


# class ProductUpdateSchema(ProductBaseSchema):
#     pass


class ProductReadSchema(ProductBaseSchema):
    id: ProductIdType = Field(
        example="1",
    )
    name: str = Field(example="Laptop")


class ProductSchema(ProductBaseSchema):
    id: ProductIdType
