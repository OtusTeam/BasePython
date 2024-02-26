class User:
    __slots__ = ("name", "age", "email")

    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email

    def increase_age(self):
        self.age += 1


user_john = User("John", age=42)
user_sam = User(age=55, name="Sam")
print(user_john)
print(user_john.name, user_john.age)
print(user_sam)
print(user_sam.name, user_sam.age)
user_john.increase_age()
print(user_john.name, user_john.age)

print(user_john.email)
user_john.email = "john@example.com"
print(user_john.email)
print(user_sam.email)
# print(user_sam.__dict__)
# print(vars(user_sam))
# user_sam.homepage = "www.example.com"
print(user_sam.__slots__)


print(len([1, 2, 3]))
print(len({"name": "John", "age": 42}))
print(({"name": "Sam", "age": 33}).__len__())
