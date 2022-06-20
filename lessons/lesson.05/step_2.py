
# class User(object):
class User:
    """
    My User object
    """
    name = None
    age = None


"""
# дескрипторы 
attr search:
instance
parent
parent's parent
...
"""

"""
x.y
y - атрибут объекта x
"""

print("object.__dict__", object.__dict__)

print(User.__mro__)

# NameError: name 'age' is not defined
# print(age)
# print(name)

user1 = User()
user1.age = 42
user1.name = "John"

user2 = User()
user2.age = 13

print("age 1", user1.age)
print("age 2", user2.age)
print("name 1", user1.name)
print("name 2", user2.name)

user3 = User()
print("name 3", user3.name)

User.name = "empty"

print("name 3", user3.name)
print("name 2", user2.name)

print("User.__dict__", User.__dict__)
print("User.__str__", User.__str__)
print("User.__str__(User)", User.__str__(User))
print("str(User)", str(User))
