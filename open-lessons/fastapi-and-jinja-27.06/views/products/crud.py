from pydantic import BaseModel

from .schemas import ProductSchema, ProductCreateSchema, ProductIdType


class ProductCRUD(BaseModel):
    id_to_product: dict[ProductIdType, ProductSchema] = {}
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def products_list(self) -> list[ProductSchema]:
        return list(self.id_to_product.values())

    def product_details(self, product_id: int) -> ProductSchema | None:
        return self.id_to_product.get(product_id)

    def create_product(self, product_in: ProductCreateSchema) -> ProductSchema:
        product = ProductSchema(
            id=self.next_id,
            **product_in.model_dump(),
        )
        self.id_to_product[product.id] = product
        return product


storage = ProductCRUD()

storage.create_product(
    ProductCreateSchema(
        name="Desktop",
        price=1234,
    )
)
storage.create_product(
    ProductCreateSchema(
        name="Laptop",
        price=1122,
    )
)
storage.create_product(
    ProductCreateSchema(
        name="Smartphone",
        price=999,
    )
)
