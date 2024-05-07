"""
Create
Read
Update
Delete
"""

from sqlalchemy import select

from models import db, Product


def create_product(name: str) -> Product:
    product = Product(name=name)
    db.session.add(product)
    db.session.commit()
    return product


def get_products() -> list[Product]:
    # return list(Product.query.all())
    return list(db.session.scalars(select(Product)).all())


# def get_product(product_id: int) -> Product | None:
#     return db.session.get(Product, product_id)
# return Product.query.get(product_id)
