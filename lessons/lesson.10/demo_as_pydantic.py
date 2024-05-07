from typing import Annotated
from annotated_types import Ge
from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict,
    Field,
    PositiveInt,
    field_validator,
)


class Person(BaseModel):
    model_config = ConfigDict(
        # strict=True,
        # frozen=True,
        # str_max_length=20,
        # str_to_lower=True,
        # str_to_upper=True,
    )

    name: str = Field(..., min_length=3, max_length=20)
    age: Annotated[int, Ge(13)]
    email: EmailStr

    @field_validator("name")
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        # if ' ' not in v:
        #     raise ValueError('must contain a space')
        return v.title()

    def increase_age(self):
        self.age += 1


class Grocery(BaseModel):
    name: str
    weight: PositiveInt
    tags: list = ["sale"]
    # tags: list = Field(default_factory=list)


def main():
    person = Person(
        name="John",
        age="42",
        email="john@example.com",
    )
    print(person)
    person.increase_age()
    print(person)

    print(person.model_dump())
    p = Person.model_validate({
        'name': 'john smith',
        'age': "43",
        'email': 'john@example.com',
    })
    print(p)
    person.name = p.name
    print("p == person", p == person)
    p.increase_age()
    print("p == person", p == person)

    # Person(name="Jo", age=10, email="a@abc.com")

    print()

    bread = Grocery(name="Bread", weight=200)
    milk = Grocery(name="Milk", weight=930)
    choco = Grocery(name="Choco", weight=100, tags=["sugar"])
    print(bread)
    print(milk)
    print(choco)

    print([bread, milk, choco])

    bread.tags.append("wheat")
    milk.tags.append("whole")
    print(bread)
    print(milk)


if __name__ == "__main__":
    main()
