from dataclasses import dataclass, field, asdict, astuple


@dataclass
class Point:
    x: int
    y: int


@dataclass(slots=True)
class Person:
    # name: str
    age: int
    weight: int
    price: int = 0
    # numbers: list[int] = []
    numbers: list[int] = field(default_factory=list)
    # numbers: list[int] = field(default_factory=lambda: [1, 2, 3])

    def increase_age(self):
        self.age += 1


@dataclass(frozen=True)
class Food:
    name: str
    weight: int


def main():
    p1 = Point(3, 5)
    print(p1)
    p2 = Point(x=2, y=4)
    print(p2)

    print("p1 == p2", p1 == p2)

    p3 = Point(p1.x, p1.y)
    print(p3)
    print("p3 == p1", p3 == p1)
    print("p1 is p3", p1 is p3)
    p4 = p1
    print("p1 is p4", p1 is p4)

    person = Person(age=3, weight=5)
    # age, weight = person
    print(person)
    print(p1)
    print("p1 == person", p1 == person)
    # person = Person(name="John", age=42)
    # print(person)
    person2 = person
    person.age = 42
    person2.weight = 55
    print(person)
    person.increase_age()
    print(person2)

    # print(person.__slots__)
    # person.email = "person@email.com"
    # print(person.email)

    milk = Food("Milk", 950)
    bread = Food("Bread", 400)
    print(milk)
    print(bread)
    # bread.weight = 350
    # bread.price = 100
    print("compare milk")
    print(("Milk", 950) == milk)
    print(("Milk", 950) == astuple(milk))
    cookies = Food("Cookie", weight="333g")
    print(cookies)

    print()
    print(asdict(cookies))
    print(astuple(cookies))


if __name__ == "__main__":
    main()
