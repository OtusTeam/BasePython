class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self.age})"

    def inc_age(self):
        self.age += 1

    def __str__(self):
        return self.full_name


user_john = User("John", "Doe", 25)
# user_john.age = 26
user_john.inc_age()
print(user_john, user_john.age)
