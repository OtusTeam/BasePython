from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from random import randint

app = FastAPI()


class ProductUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


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


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/contact/")
async def contact():
    return {"message": "Hello contact"}


@app.get("/products/{product_id}")
async def read_product(product_id: str):
    return {"product_id": product_id}


@app.get("/users/{user_id}/{uid_id}")
async def read_user(user_id: int, uid_id: str):
    user_id += 100
    uid_id = f'Ваш номер - {uid_id}'
    return {"user id": user_id, "uid": uid_id}


@app.get("/products/")
async def list_product(discount: Optional[bool] = None):
    if discount:
        for product in products:
            if product.price < 1000:
                product.description = "Распродажа"
        return {"discount": products}
    return {"discount": products}


@app.post("/products/")
async def create_product(product: Product):
    products.append(product)  # products.append(product)
    return {"product": product}


@app.put("/products/{product_id}")
async def update_product(product_id: int, update_product: ProductUpdate):
    for product in products:
        if product.pk == product_id:
            product.name = update_product.name
            product.price = update_product.price
            product.description = update_product.description
            return {'Message': f'Объект {product} обновлен'}

    return {"Message": 'Объект не найде'}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for product in products:
        if product.pk == product_id:
            products.remove(product)
            return {'Message': f'Объект {product} удален'}

    return {"Message": 'Объект не найден'}