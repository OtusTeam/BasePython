from dataclasses import dataclass, field


@dataclass(slots=True)
class Product:
    id: int
    name: str
    # price: int


@dataclass
class ProductsStorage:
    last_id: int = 0
    products: dict[int, Product] = field(default_factory=dict)

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    def get_products_list(self) -> list[Product]:
        return list(self.products.values())

    def get_product_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)

    def create_product(self, name: str) -> Product:
        product = Product(
            id=self.next_id,
            name=name,
        )
        self.products[product.id] = product
        return product

    def delete_product(self, product_id: int) -> None:
        self.products.pop(product_id, None)


storage = ProductsStorage()

storage.create_product("Desktop")
storage.create_product("Laptop")
