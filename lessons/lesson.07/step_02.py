class User:
    pass


user_john = User()
user_sam = User()
print(type(user_john))
print(type({}))
user_john.name = "John"
user_john.email = "john@example.com"
user_sam.name = "Sam"
print(user_john)
print(user_sam)
print(user_john.name)
print(user_john.email)
print(user_sam.name)

user_nick = User()
print(user_nick.name)
