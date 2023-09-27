from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(str_to_lower=True)

    username: str = Field(min_length=3, max_length=30)
    email: str


class Grocery(BaseModel):
    model_config = ConfigDict(
        # strict=False,
        validate_assignment=True,
        # frozen=True,
    )

    weight: int
    price: int = Field(ge=1, lt=1000)
    best_before: datetime = Field(default_factory=datetime.now)
    # production_dt: datetime = datetime.now

    tags: list[str] = ["sale"]

    @property
    def sale_price(self):
        return self.price * 0.9


def main():
    # bread = Grocery(weight=600, price=b"40")
    bread = Grocery(weight=600, price=40, best_before=1695839613)
    bread.tags.append("eat")
    print(bread)
    # milk = Grocery(weight=900, price="99")
    milk = Grocery(weight=900, price=99)
    milk.tags.append("drink")
    print(milk)
    meat = Grocery(weight=1000, price=999, tags=["chicken"])
    print(meat)
    meat.price = 800
    print(meat)
    print(meat.sale_price)
    print(meat.model_dump())
    print(meat.model_dump_json())

    grocery_data = {
        "weight": 700,
        "price": 90,
        "best_before": "2023-09-28T21:00:00",
        "tags": [],
    }
    # grocery = Grocery(**grocery_data)
    grocery = Grocery.model_validate(grocery_data)
    print(grocery)
    # g_json = '{"weight":1000,"price":800,"best_before":"2023-09-27T21:26:15.245609"}'
    g_json = '{"weight":1000,"price":800,"best_before":1695839913}'
    g = Grocery.model_validate_json(g_json)
    print("g:", g)

    sam = User(username="Sam", email="Sam@example.COM")
    print(sam)
    print(bread.best_before.isoformat())
    print(bread.best_before.timestamp())


if __name__ == "__main__":
    main()
