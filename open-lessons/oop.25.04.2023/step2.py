class User:
    def __init__(
        self,
        name: str,
        username: str | None = None,
        age: int | None = None,
    ):
        self.name = name
        self.username = username
        self.age = age

    def increase_age(self):
        if self.age is not None:
            self.age += 1
        else:
            self.age = 0


print(User.__dict__)

john = User(name="John")
print("john", john, john.__dict__)

sam = User(name="Sam", username="sam3000")
print(sam.name)
print("sam", sam, sam.__dict__)
print("sam name:", sam.name)
print("sam username:", sam.username)
# sam.username = "sam3000"
# print("sam", sam, sam.__dict__)

print(sam.age)
sam.increase_age()
print(sam.age)
sam.increase_age()
print(sam.age)
sam.increase_age()
print(sam.age)

