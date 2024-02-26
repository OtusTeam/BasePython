class User:
    pass


def init_user(user: User, name, age):
    user.name = name
    user.age = age
    return user


user_john = User()
init_user(user_john, name="John", age=42)
user_sam = User()
init_user(user_sam, name="Sam", age=55)
print(user_john)
print(user_john.name, user_john.age)
print(user_sam)
print(user_sam.name, user_sam.age)

user_nick = User()
init_user(user_nick, name="Nick", age=15)
print(user_nick.name, user_nick.age)
