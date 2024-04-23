class User:
    def __init__(self, name, age, address=None, password=None):
        self.name = name
        self._age = int(age)
        self.address = address
        self._password = self._abcde(password)

    def set_older(self):
        self._age += 1

    def _abcde(self, password):
        pass


user_1 = User('Ivan', '25')

# user_1.age = '27'
# user_1.hash_password('hello')

print(vars(user_1))
user_1.set_older()
print(vars(user_1))
