class User:
    def __init__(self, name, age=None):
        self.name = name
        self._age = int(age)  # protected

    @property
    def age(self):
        return self._age

    def set_older(self):
        self._age += 1


# user_1 = User('Vlad', 38)
user_1 = User('Vlad', '38')
# user_1 = User('Vlad', '38 years')

# user_1.age = 40
print(vars(user_1))
# print(user_1.age)
# user_1.age = '40'  # set
# print(vars(user_1))
# print(user_1.age)  # get
user_1.set_older()
print(user_1.age)
# print(user_1.age())
