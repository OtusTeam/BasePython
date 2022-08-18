"""
This is a documentation string
"""

some_object = object()
print(some_object)

a = 1
print(type(a))
b = ''
print(type(b))

c = int()
d = str()

print(type(c))
print(type(d))


# class User(object):
class User:
    """
    Doc string for user
    """


print(int)
print(User)

user1 = User()
print(user1)
print(type(user1))

user1.name = "John"
print("user name:", user1.name)
print("user1 dict", user1.__dict__)

user2 = User()
user2.name = "Sam"
print("user2 name", user2.name)
print("user2 dict", user2.__dict__)
user2.age = 20
print("user2 age", user2.age)
print("user2 dict", user2.__dict__)

print("user1 dict", user1.__dict__)
print(User.mro())

# print("user1 age", user1.age)


# print("__name__:", __name__)

