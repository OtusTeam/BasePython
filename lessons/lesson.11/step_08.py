import secrets
from hashlib import md5


class User:
    def __init__(self, username: str) -> None:
        self.username = username
        self.password = secrets.token_urlsafe(10)

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        self.__password = md5(value.encode()).hexdigest()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(username={self.username!r})"


class SuperUser(User):
    def act(self, superaction):
        print(self, "doing superaction", superaction)


bob = User("bob")
print(bob)
print("username:", bob.username)
print("password:", bob.password)
# bob.__password = "bbb"
# print("password:", bob.password)
# print("bob.__password:", bob.__password)
# bob._User__password = "ccc"
# print("password:", bob.password)

bob.password = "ddd"
print("password:", bob.password)
bob.password = "1"
print("1:", bob.password)
bob.password = "0"
print("0:", bob.password)

print("bob's dict:", bob.__dict__)

admin = SuperUser("admin")
print(admin)
admin.act("qwerty")

print("admin.password:", admin.password)
admin.password = "adminadmin"
print("admin.password:", admin.password)

print(admin.__dict__)
