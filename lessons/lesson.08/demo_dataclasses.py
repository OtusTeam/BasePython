from dataclasses import dataclass, asdict, astuple, field


@dataclass
class Point:
    x: int
    y: int
    z: int


@dataclass
class Person:
    age: int
    weight: int
    fat: int


@dataclass
class User:
    id: int
    name: str
    # username: str
    email: str = field(default=None)


def factory_categories() -> list[str]:
    return ["sale"]


@dataclass(frozen=True)
class Product:
    weight: int
    price: float

    # categories: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=factory_categories)


def demo_persons_and_points():
    admin = User(1, name="admin")
    print("admin.email", admin.email)
    # john = User("qwe", name="john", email=123456)
    john = User(2, name="john", email="john@example.com")
    print(admin)
    print(john)
    point = Point(30, 95, 42)
    point2 = Point(30, 95, 42)
    person = Person(30, 95, 42)
    print(point)
    print(person)
    print("point == person", point == person)
    print("point == point2", point == point2)
    # point2.z = 10
    # print(point2)
    # print("point == point2", point == point2)
    # print(asdict(person))
    # print(asdict(point))
    # print(astuple(person))
    # print(astuple(point))


def are_points_similar(p1: Point, p2: Point) -> bool:
    return p1.x == p2.x


def main():
    demo_persons_and_points()
    bread = Product(400, 50)
    milk = Product(900, 99)
    milk.categories.append("milk")
    bread.categories.append("wheat")
    print(milk)
    print(bread)
    # bread.price = 60
    # print(bread)
    # print({}["we"])
    bread2 = Product(weight=bread.weight, price=bread.price * 1.2, categories=list(bread.categories))
    print(bread2)
    print(bread2.categories.append("cat2"))
    print(bread2)
    print(bread)
    print(bread.price / bread.weight)
    # print(bread.price / bread.categories)


if __name__ == '__main__':
    main()

