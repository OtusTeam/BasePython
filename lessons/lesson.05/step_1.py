class User:
    name = None
    age = None


print(User.mro())

user1 = User()
print("user1 name", user1.name)
print(user1.__dict__)
user1.name = "john"
print("user1 name", user1.name)
print(user1.__dict__)


user2 = User()
print("user2 name", user2.name)
print(user2.__dict__)
user2.name = "sam"
user2.age = 20
print("user2 name", user2.name)
print(user2.__dict__)
print("user2 age", user2.age)

user3 = User()
print("user3 name", user3.name)
print(user3.__dict__)
print("user3 age", user3.age)

User.name = "Nick"

print("user3 name", user3.name)
print(user3.__dict__)

print("user2 name", user2.name)
print("user1 name", user1.name)


print(None)
print(type(None))
print(False)
print(type(False))
print(True)
print(type(True))
print(1)
print(type(1))


# class MyNone(type(None)):
#     pass
