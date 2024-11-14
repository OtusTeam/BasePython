"""
CRUD functions for products

Create
Read
Update
Delete
"""

from random import randint

from sqlalchemy import select, exists, func

from models import db, Product


class ProductsStorage:

    def create(self, name: str, price: int | None = None) -> Product:
        product = Product(
            name=name,
            price=price or randint(10, 1000),
        )
        db.session.add(product)
        db.session.commit()
        return product

    def get(self) -> list[Product]:
        results = db.session.scalars(select(Product).order_by("id")).all()
        return list(results)

    def get_by_id(self, product_id: int) -> Product | None:
        return db.session.get(Product, ident=product_id)

    def delete(self, product: Product) -> None:
        db.session.delete(product)
        db.session.commit()

    def name_exists(self, product_name: str) -> bool:
        stmt = exists().where(
            func.lower(Product.name) == product_name.lower(),
        )
        return db.session.scalar(select(stmt))


products_storage = ProductsStorage()
