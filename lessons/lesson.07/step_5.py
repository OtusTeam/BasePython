class User:
    def __init__(self, name, age, address=None):
        self.name = name
        # self.age = int(age)
        self._age = int(age)
        self.address = address

    def set_older(self):
        self._age += 1


user_1 = User('Ivan', '25')
...
# user_1.age = 27
# print(user_1.age)

user_1.age = '27'
# user_1._age = '27'

print(vars(user_1))
user_1.set_older()
print(vars(user_1))
