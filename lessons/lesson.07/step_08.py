class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(first_name={self.first_name!r},"
                f" last_name={self.last_name!r})")


user_john = User("John", "Doe")
user_sam = User("Sam", "White")
print(user_john)
print(str(user_john))
print(user_sam)
print([user_john, user_sam])

print(user_sam.first_name)
print(user_sam.last_name)
print(user_sam.full_name)
print(repr(user_sam))
user_sam.last_name = "Black"
print(repr(user_sam))
print(user_sam.first_name)
print(user_sam.last_name)
print(user_sam.full_name)
