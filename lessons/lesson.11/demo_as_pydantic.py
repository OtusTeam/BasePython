from datetime import datetime, date

# from annotated_types import Gt, Lt, MinLen, MaxLen
from pydantic import BaseModel, PositiveInt, ConfigDict, Field


class Food(BaseModel):
    name: str = Field(minlength=3, max_length=10)
    weight: PositiveInt
    best_before: date = Field(default_factory=date.today)
    tags: list[str] = ["sale"]


class Person(BaseModel):
    model_config = ConfigDict(
        # strict=False,
        # frozen=True,
        str_max_length=20,
    )

    name: str
    age: PositiveInt
    email: str | None = None

    # favorite_food: Food | None = None

    def increase_age(self):
        self.age += 1



def main():
    p = Person(
        name=b"Sam Black",
        age="42",
        email="sam@example.com",
    )
    print(p)
    print([p])
    print(repr(p))
    p.name = "Sam Grey"
    print(p)
    p.increase_age()
    print(p)

    print()
    salad = Food(name="Salad", weight=200)
    pie = Food(name="Pie", weight=500, tags=["sugar"])
    print(salad)
    print(pie)
    cookies = Food(name="Cookies", weight=300)
    print(cookies)
    cookies.tags.append("sugar")
    print(salad)
    print(cookies)


if __name__ == "__main__":
    main()
