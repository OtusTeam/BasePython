"""
Create
Read
Update
Delete
"""

from dataclasses import dataclass
from dataclasses import asdict
from dataclasses import field

from .models import Product, ProductCreate


@dataclass
class ProductsStorage:
    products: dict[int, Product] = field(default_factory=dict)
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create(self, product_create: ProductCreate) -> Product:
        product = Product(
            id=self.next_id,
            **asdict(product_create),
        )
        self.products[product.id] = product
        return product

    def get(self) -> list[Product]:
        return list(self.products.values())

    def get_by_id(self, user_id: int) -> Product | None:
        return self.products.get(user_id)


storage = ProductsStorage()
storage.create(
    ProductCreate(
        name="Smartphone",
        price=999,
    ),
)
storage.create(
    ProductCreate(
        name="Laptop",
        price=1999,
    ),
)
storage.create(
    ProductCreate(
        name="Tablet",
        price=699,
    ),
)
