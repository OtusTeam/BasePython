from fastapi import APIRouter
from pydantic import BaseModel, Field

from typing import Optional
from random import randint


router = APIRouter()


class ProductUpdate(BaseModel):
    name: str = Field(..., title='Product Name',  min_length=3, max_length=10)
    description: Optional[str] = Field(None, title='Description', max_length=1000)
    price: float = Field(..., title='Product Price', ge=0, le=100_000)


class Product(ProductUpdate):
    pk: int



products = []

for i in range(10):
    products.append(Product(
        pk=i,
        name=f'Продукт {i}',
        description=f'Описание продукта {i}',
        price=randint(100, 5000)))


# print(products)


@router.get("/products/{product_id}")
async def read_product(product_id: str):
    return {"product_id": product_id}

@router.get("/users/{user_id}/{uid_id}")
async def read_user(user_id: int, uid_id: str):
    user_id += 100
    uid_id = f'Ваш номер - {uid_id}'
    return {"user id": user_id, "uid": uid_id}


@router.get("/products/")
async def list_product(discount: Optional[bool] = None):
    if discount:
        for product in products:
            if product.price < 1000:
                product.description = "Распродажа"
        return {"discount": products}
    return {"discount": products}


@router.post("/products/")
async def create_product(product: Product):
    products.append(product)  # products.append(product)
    return {"product": product}


@router.put("/products/{product_id}")
async def update_product(product_id: int, update_product: ProductUpdate):
    for product in products:
        if product.pk == product_id:
            product.name = update_product.name
            product.price = update_product.price
            product.description = update_product.description
            return {'Message': f'Объект {product} обновлен'}

    return {"Message": 'Объект не найде'}


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for product in products:
        if product.pk == product_id:
            products.remove(product)
            return {'Message': f'Объект {product} удален'}

    return {"Message": 'Объект не найден'}