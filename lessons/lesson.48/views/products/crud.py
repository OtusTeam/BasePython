"""
CRUD functions for products

Create
Read
Update
Delete
"""

from dataclasses import dataclass, field
from random import randint


@dataclass
class Product:
    id: int
    name: str
    price: int


@dataclass
class ProductsStorage:
    products: dict[int, Product] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create(self, name: str, price: int | None = None) -> Product:
        product = Product(
            id=self.next_id,
            name=name,
            price=price or randint(10, 1000),
        )
        self.products[product.id] = product
        return product

    def get(self) -> list[Product]:
        return list(self.products.values())

    def get_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)


products_storage = ProductsStorage()
products_storage.create(name="Laptop")
products_storage.create(name="Desktop")
products_storage.create(name="Tablet")
