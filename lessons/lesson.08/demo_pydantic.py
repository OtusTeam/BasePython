from datetime import datetime

from pydantic import BaseModel, Extra, conint, constr, Field


class Point(BaseModel):
    x: int
    y: int

    class Config:
        frozen = True


class PersonConfig:
    frozen = True


class Person(BaseModel):
    age: int
    name: str
    email: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    favourite_numbers: set[int] = {42, 55}

    # Config = PersonConfig

    class Config:
        extra = Extra.ignore
        # extra = Extra.allow
        # extra = Extra.forbid
        # frozen = True
        # allow_mutation = False


class Food(BaseModel):
    # name: str
    name: constr(min_length=3, max_length=20)
    # price: int
    price: conint(gt=0, le=1000)
    weight: float

    class Config:
        # frozen = True
        validate_assignment = True


def main():
    p1 = Point(x=1, y=2)
    print(p1)
    p2 = Point(x=3, y=4)
    print(p2)

    print([p1, p2])

    print(p1 == p2)
    p3 = p1
    print(p3)
    print(p1 == p3)
    print(p1 is p3)

    person_john = Person(
        age=42,
        name="John",
        weight="12345",
        # created_at="2022-11-23T17:49:50",
        created_at=1669214090,
        favourite_numbers=["1", b"42", 3],
    )
    print(person_john)
    person_john.email = "john@example.com"
    print(person_john)
    print(person_john.favourite_numbers)
    person_john.favourite_numbers.add(5)
    print(person_john.favourite_numbers)
    print(person_john.created_at.timestamp())
    # print(person_john.weight)

    sam = Person(
        name="Sam",
        age=42,
    )
    nick = Person(
        name="Nick",
        age=30,
    )
    print(sam)
    print(nick)
    sam.favourite_numbers.add(7)
    nick.favourite_numbers.add(42)
    nick.favourite_numbers.add(33)

    print(sam)
    print(nick)

    milk = Food(name="Milk", price=1, weight=b"200")
    milk.name = "Whole Milk"
    # milk.price = 1001
    milk.price = 1000
    print(milk)
    print(repr(milk.dict()))
    print(repr(milk.json()))
    print(nick.dict())
    print(nick.json())


if __name__ == "__main__":
    main()
