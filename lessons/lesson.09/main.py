from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

User = namedtuple('User', 'user_id, age, username, email, full_name')

# class NewUser(User):
#     def abc(self):
#         pass

UserIdAndAge = namedtuple('UserIdAndAge', ['user_id', 'age'])

# u = User
# print("u:", u)

# class User:
#     pass
#
#
# User = type('User', (object, ), {})


def demo_point():
    p1 = Point(1, 2)
    p2 = Point(x=3, y=4)
    p3 = Point(5, y=6)

    print(p1)
    print(p2)
    print(p3)

    print(p1.x + p2.x)
    print(p1.y + p2.y)
    print(p2[0], p3[0])
    print(p2[1], p3[1])


def demo_user():
    """
    :return:
    """
    u = User(
        user_id=1,
        age=14,
        username="john",
        email="john@example.com",
        full_name="John Smith",
    )
    # func call..
    #
    user_id, age, username, email, full_name = u
    print(user_id)
    print(age)
    print(username)

    print(u)
    print(u[3], u.email)
    print("as dict:", u._asdict())
    print(type(u), u.__class__.mro())
    print(type(User))
    print(type(object))
    print(type(type))


def demo_multi():
    id_and_age = UserIdAndAge(123, 21)
    print(id_and_age)
    p = Point(123, 21)
    print(p)
    print("id_and_age == p:", id_and_age == p)
    print("(1, 2) == (1, 2):", (1, 2) == (1, 2))
    print(UserIdAndAge(1, 2) == Point(2, 1))
    #
    t1 = tuple(id_and_age)
    t2 = tuple(p)
    print(t1, t2)
    print("t1 == t2", t1 == t2)
    print('(1, "abc") == (1, "abc")', (1, "abc") == (1, "abc"))
    p1 = Point(1, "abc")
    id_and_age1 = UserIdAndAge(1, "abc")
    print(p1, id_and_age1)
    print("p1 == id_and_age1", p1 == id_and_age1)
    print("t1 is t2", t1 is t2)
    print(User)


def main():
    # demo_point()
    # demo_user()
    demo_multi()


if __name__ == '__main__':
    main()
    # NewUser
