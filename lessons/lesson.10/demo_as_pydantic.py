from typing import Annotated

from annotated_types import Ge, MaxLen
from pydantic import ConfigDict, Field
from pydantic import PositiveInt
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import StringConstraints


class Person(BaseModel):
    name: Annotated[
        str,
        StringConstraints(min_length=3, max_length=120),
    ]
    age: Annotated[int, Ge(13)]
    email: Annotated[
        EmailStr,
        MaxLen(100),
    ]

    def increase_age(self):
        self.age += 1


class Food(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        # strict=True,
        str_to_lower=True,
        str_strip_whitespace=True,
    )

    name: Annotated[
        str,
        StringConstraints(min_length=3, max_length=120),
    ]
    description: str = ""
    weight: PositiveInt
    price: PositiveInt
    # tags: list[str] = Field(default_factory=list)
    tags: list[str] = ["sale"]


def get_person() -> Person:
    return Person(
        name="John",
        age=25,
        email="john@example.com",
    )


def main():
    person = get_person()
    print(person)
    print("name:", person.name)
    print("age:", person.age)
    print("email:", person.email)

    person.increase_age()
    print("age:", person.age)

    sam = Person(name="Sam", age="42", email="sam@example.com")
    # sam = Person(name="Sam", age="42", email=email)
    print(sam)
    print(sam.email)

    bread = Food(name="Bread", weight="500", price=100)
    bread.tags.append("bread")
    # bread.tags.append("sale")
    print(bread)
    # bread.weight -= 50
    # print(bread)

    milk = Food(name="Milk", weight="500", price=100, description=" whole Milk!   ")
    milk.tags.append("milk")
    print(milk)


if __name__ == "__main__":
    main()
