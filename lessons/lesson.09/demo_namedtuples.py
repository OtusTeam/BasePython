from collections import namedtuple

User = namedtuple("User", "id, age, name")

Car = namedtuple("Car", "manufacturer, age")
Book = namedtuple("Book", "author, copies")


def get_user():
    user_id = 7
    user_age = 15
    user_name = "sam"
    return User(user_id, user_age, user_name)


def demo_car_and_book():
    car = Car("Ford", 2000)
    print(car)
    book = Book("Ford", 2000)
    print(book)

    car_1 = ("A", 123)
    book_1 = ("A", 123)
    print("car_1 == book_1", car_1 == book_1)
    print("car == book", car == book)
    print("(1, 2) == (1, 2)", (1, 2) == (1, 2))


def main():
    demo_car_and_book()
    return
    print(User.mro())
    user = get_user()
    print(user)
    print(user[0])
    print(user[1])

    print(user.name)
    print(user.age)


# print("top level")
if __name__ == '__main__':
    # print("only if main")
    main()
