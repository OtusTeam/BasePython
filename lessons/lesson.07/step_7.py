class User:
    def __init__(self, name, age, address=None):
        self.name = name
        # _age = int(age)
        # if _age < 0:
        #     raise ValueError
        # self._age = _age
        self._age = int(age)
        self.address = address

    @property
    def age(self):  # getter
        return self._age
        # return f'{self._age} year(s)'

    # def get_age(self):
    #     return self._age

    def set_older(self):
        self._age += 1


user_1 = User('Ivan', '25')

# print(user_1.age())
print(user_1.age)
# user_1.age = '27'
