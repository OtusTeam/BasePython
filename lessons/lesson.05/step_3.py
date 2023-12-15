class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def set_older(self, age_diff=1):
        self.age += age_diff


user_1 = User('Vlad', 38)
user_2 = User('Olga')
print(user_1)
print(vars(user_1))
user_1.set_older()
print(vars(user_1))
print(user_1.name)
print(user_1.age)
