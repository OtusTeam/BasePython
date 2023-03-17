class User:
    def __init__(self, name, age):
        self.name = name
        self._age = int(age)

    @property
    def age(self):
        return self._age

    # def set_age(self, age):
    #     # assert isinstance(age, int), f'wrong type of age: {type(age)}'
    #     self._age = int(age)

    def year_older(self):
        self._age += 1


user_1 = User('Ivan', '25')

print(user_1.age)
user_1.name = 'Boris'
# user_1.age = '25 years'
user_1.year_older()
user_1.year_older()
user_1.year_older()
print(user_1.age)
print(user_1.name)

# print(user_1.get_age())
# # user_1.set_age('25 years')
# user_1.set_age('25')
# user_1.age = '25 years'
# user_1.year_older()
# print(user_1.get_age())
# print(vars(user_1))
