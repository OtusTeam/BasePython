from dataclasses import dataclass, asdict, astuple, field


@dataclass
class Point:
    x: int
    y: int


@dataclass(slots=True, kw_only=True)
class Person:
    age: int
    weight: int
    # email: Optional[str] = None
    email: str | None = None

    def increase_age(self):
        self.age += 1
        return self.age


@dataclass(frozen=True)
class Product:
    name: str
    weight: int
    price: int
    tags: list[str] = field(default_factory=list)


#


def get_point():
    return Point(20, 70)


def get_person():
    return Person(age=20, weight=70, email="a@b.c")


def main():
    p1 = get_point()
    print(p1)
    person_1 = get_person()
    print(person_1)
    print("person_1 == p1:", person_1 == p1)
    person_1.email = "john@b.c"
    print(person_1)

    milk = Product("milk", 1000, 80)
    bread = Product("bread", 400, 50)
    print(milk)
    milk.tags.append("tag1")
    print(milk)
    print(bread)

    # bread.price = 100
    print(person_1)
    person_1.increase_age()
    print(person_1)
    # person_1.credit = 10000
    # print(person_1.credit)
    print(asdict(person_1))
    print(astuple(person_1))


if __name__ == "__main__":
    main()
