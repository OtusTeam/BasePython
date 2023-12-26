from datetime import datetime, timedelta
from typing import Annotated

from annotated_types import Ge, Lt
from pydantic import BaseModel, Field, ConfigDict


class Grocery(BaseModel):
    model_config = ConfigDict(
        # validate_assignment=True,
        frozen=True,
        str_strip_whitespace=True,
    )
    title: str
    weight: Annotated[int, Ge(1), Lt(10_000)]
    price: int = Field(ge=1, lt=1000)
    # tags: list[str] = Field(default_factory=list)
    # tags: list[str] = Field(default_factory=lambda: ["sale"])
    tags: list[str] = ["sale"]
    best_before: datetime = Field(
        default_factory=lambda: datetime.now() + timedelta(days=7)
    )

    @property
    def sale_price(self):
        return self.price * 0.9


def main():
    milk = Grocery(
        title="Whole Milk ",
        weight=b"1000",
        price="77",
        best_before="2023-12-29T12:30:42",
    )
    bread = Grocery(
        title="White bread",
        weight=500,
        price=100,
        # tags=["abc", b"qwe"],
        best_before=1703842130,
    )
    print(milk)
    print(bread)
    print(repr(milk))
    print(milk.weight)
    print(type(milk.weight))
    # milk.weight = "123g"
    # print(milk.weight)
    # print(type(milk.weight))

    milk.tags.append("pancakes")
    bread.tags.append("today")
    print(milk.tags)
    print(bread.tags)
    print()

    print(milk.sale_price)
    print(milk.best_before.timestamp())
    print(bread.sale_price)


if __name__ == "__main__":
    main()
