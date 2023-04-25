print("Hello world!")

some_object = object()

print(some_object)


def my_func():
    print("hello")
    # return "abc"
    # return None
    # return


print(my_func)

res = my_func()
print("result:", res)


class MyObject(object):
    pass


print(object)
print(MyObject)
my_obj = MyObject()
print(some_object)
print(my_obj)

print("MyObject mro", MyObject.mro())


class User:
    pass


user = User()
print(User)
print(user)
print("user type:", type(user))
print("User type:", type(User))

print("User mro", User.mro())

line_hello = "hello"
# line_hello = str("hello")
print(line_hello)
line_hello_type = type(line_hello)
print(line_hello_type)
print(line_hello_type is str)
print("str type:", type(str))
print("type is type", type(str) is type)
print("type mro", type.mro(type))
print("type object", type(object))


john = User()
print("john dict", john.__dict__)
# print("john name", john.name)
john.name = "John"
print("john:", john, john.name)
print("john dict", john.__dict__)


sam = User()
print("sam dict", sam.__dict__)

sam.username = "sam3000"
print("sam:", sam, sam.username)
# print("sam:", sam, sam.name)

print("john dict", john.__dict__)
print("sam dict", sam.__dict__)
