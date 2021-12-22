from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    age: int
    name: str
    friends: list[int] = field(default_factory=list)

    def increase_age(self):
        self.age += 1


@dataclass
class Car:
    manufacturer: str
    year: int


@dataclass
class Book:
    author: str
    copies: int


@dataclass
class SportCar(Car):
    turbines: int


@dataclass(frozen=True)
class Food:
    name: str
    weight: int


def demo_food():
    milk = Food("milk", 950)
    bread = Food("bread", 300)

    print(bread)
    print(milk)
    try:
        milk.weight = 900
    except Exception:
        print("error")
    print(milk)
    milk2 = Food("milk", 950)
    print("milk2 == milk", milk2 == milk)
    milk3 = Food("milk", 900)
    print("milk3 == milk2", milk3 == milk2)


def get_user():
    user_id = 7
    user_age = 15
    some_name = "sam"
    return User(user_id, user_age, some_name)


def demo_car_and_book():
    car = Car("Ford", 2000)
    book = Book("Ford", 2000)
    print(car)
    print(book)

    print("car == book", car == book)


def demo_sportcar():
    sportcar = SportCar(year=2020, turbines=8, manufacturer="Ford")
    print(sportcar)


def main():
    print(User.mro())
    demo_food()
    demo_sportcar()
    demo_car_and_book()

    user = get_user()
    print(user)
    user.increase_age()
    print(user)


if __name__ == '__main__':
    main()
