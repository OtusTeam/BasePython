"""
Create
Read
Update
Delete
"""
from dataclasses import dataclass, field


@dataclass
class Product:
    id: int
    name: str
    # price: int


@dataclass
class Storage:
    products: dict[int, Product] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create_product(self, name: str) -> Product:
        product: Product = Product(id=self.next_id, name=name)
        self.products[product.id] = product
        return product

    def get_products(self) -> list[Product]:
        return list(self.products.values())

    def get_product(self, product_id: int) -> Product | None:
        return self.products.get(product_id)


storage = Storage()

storage.create_product("Laptop")
storage.create_product("Desktop")
storage.create_product("Phone")
