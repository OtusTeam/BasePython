

# def init_user(user: "User", name, age):
#     user.name = name
#     user.age = age

# line = ('abc' "foobar" '''spam and eggs''' """ fizz buzz""")
# print(repr(line))
class User:
    # 'abc' "foobar" '''spam and eggs''' """ fizz buzz"""
    """User cls"""

    # dunder method =
    # double underscore
    #  == magic method
    def __init__(self, name, age):
        """Init function"""
        self.name = name
        self.age = age
    # __init__ = init_user

    def increase_age(self):
        self.age += 1
        # return self.age


user_john = User("John", age=42)
print(user_john.increase_age)
user_sam = User(age=55, name="Sam")
print(user_john)
print(user_john.name, user_john.age)
print(user_sam)
print(user_sam.name, user_sam.age)

#

user_nick = User(name="Nick", age=15)
print(user_nick.name, user_nick.age)
print(user_nick.__dict__)
print("user vars:")
print(vars(user_nick))
print(User.__dict__)
print(User.__init__.__doc__)

print("john.age:", user_john.age)
print("sam.age:", user_sam.age)
user_john.increase_age()
print("john.age:", user_john.age)
print("sam.age:", user_sam.age)
print(User.__dict__)
print(User.increase_age)

print("sam.age:", user_sam.age)
print("nick.age:", user_nick.age)
User.increase_age(user_sam)
print("sam.age:", user_sam.age)
print("nick.age:", user_nick.age)
User.increase_age(user_nick)
print("nick.age:", user_nick.age)

company_name = "abc QWE inc."
print(company_name)
print(company_name.title())
print(str.title(company_name))
method = str.lower
# method = str.upper
print(list(map(method, [user_john.name, user_sam.name])))
users = [user_john, user_sam]
print([user.name.title() for user in users])
