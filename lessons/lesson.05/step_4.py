class User:
    MIN_AGE = 21

    def __init__(self, name, age=None, skill=None):
        self.name = name
        self.age = age
        self.skill = skill
        self.address = None


user_1 = User(name='Ivan', skill='junior')
print(vars(user_1), id(user_1))
print(user_1.skill)
user_1.skill = 'middle'  # mutable
print(vars(user_1), id(user_1))
