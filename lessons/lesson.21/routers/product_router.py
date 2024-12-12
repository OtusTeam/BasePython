from fastapi import APIRouter
from pydantic import BaseModel, validator


router = APIRouter()


class Product(BaseModel):
    name: str
    price: float
    description: str | None = None
    image_url: str

    @validator('price')
    def check_quantity(cls, value):
        if value < 10:
            raise ValueError("Quantity must be greater than 0")
        return value


@router.post("/products/param1: int, param2: str = Qurey(...)")
async def create_products(product: Product):
    return {
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "image_url": product.image_url
    }

