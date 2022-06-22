some_object = object()
print(some_object)


# class User(object):
#     pass
#
#
# class User(object):
#     ...

"""
sdfsdfsdfg
sfgsdfg
"""


def myfunc(a, b):
    """
    my func

    эта функция помогает что-то там делать

    >>> myfunc(42, 'foobar')
    :return:
    """

    return b, a

# doc = docstring = documentation string = строка документации

help(myfunc)
print(myfunc.__doc__)


# class User(object):
#     ...
#
#
# class User:
#     pass


class User(object):
    """
    My User object
    1234567896857345674

    создаём юзера...
    """


help(User)
print(User.__doc__)

user1 = User()

print(user1)

user1.age = 42
user1.name = "John"

print(user1)

print("age", user1.age)
print("name", user1.name)

user2 = User()

user2.age = 13

print("age2", user2.age)

print("age1", user1.age)

print("age2", user2.name)

