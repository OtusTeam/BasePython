some_object = object()

print(some_object)


def myfunc():
    print("hello")


myfunc()


class MyObject(object):
    pass


# class User(object):
class User:
    pass


print(object)
print(MyObject)
print(User)


print("name:", __name__)

my_obj = MyObject()
user = User()

print(my_obj)
print(user)

print(MyObject.mro())
print(User.mro())

user.name = "John"

print(user.name)

user2 = User()
user2.name = "sam"
print(user2.name)
print(user.name)

user3 = User()
user3.name
