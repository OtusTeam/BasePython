class User:
    MIN_AGE = 21

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
print(user_john.email)
user_john.email = "john@example.com"
print(user_john.email)
print(user_sam.email)

print(User.MIN_AGE)
print(user_john.MIN_AGE)
print(user_john.__dict__)
print(User.__dict__)

user_john.MIN_AGE = 42
print(user_john.MIN_AGE)
print(user_sam.MIN_AGE)
print(user_john.__dict__)
print(User.__dict__)

print()
print(user_sam.MIN_AGE)
User.MIN_AGE = 33
print(user_sam.MIN_AGE)
print(User.__dict__)
print(User.mro())
print(User == "abc")
print(User.__eq__)
print(object.__eq__)
print("eq same?", User.__eq__ is object.__eq__)
