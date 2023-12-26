from dataclasses import dataclass, field


# @dataclass(frozen=True, slots=True)
# @dataclass(slots=True)


class Base:
    pass


@dataclass()
class Person(Base):
    name: str
    age: int
    email: str | None = None
    friends: list["Person"] = field(default_factory=list)

    def inc_age(self):
        self.age += 1


# class Person:
#     def __init__(
#         self,
#         name: str,
#         age: int,
#         email: str | None = None,
#         friends: list[int] | None = None,
#     ):
#         self.name: str = name
#         self.age: int = age
#         self.email: str | None = email
#         self.friends: list[int] = friends or []
#
#     def __str__(self):
#         ...
#
#     def __repr__(self):
#         ...
#
#     def __eq__(self, other):
#         ...


class Manager(Person):
    pass


def get_person():
    return Person(
        "John",
        age=42,
        # email=
    )


def main():
    p = get_person()
    print(p)

    p2 = get_person()
    assert p == p2
    p2.name = "Sam"
    p2.email = "sam@example.com"
    assert p != p2

    print("name:", p.name)
    print("age:", p.age)
    p.inc_age()
    print("age:", p.age)
    print("email:", p.email)
    p.email = "john@example.com"
    print("email:", p.email)

    print(p)
    # print(p.__dict__)
    p.url = "example.com"
    print(p)
    print(p.url)
    # print(p.__dict__)

    m = Manager(name="Kate", age=33)
    print(m)
    print(Person.mro())
    print(Manager.mro())


if __name__ == "__main__":
    main()
