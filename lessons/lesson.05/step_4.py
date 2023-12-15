class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = int(age)
        # self.age = age

    def set_older(self, age_diff=1):
        self.age += age_diff


# user_1 = User('Vlad', 38)
user_1 = User('Vlad', '38')
# user_1 = User('Vlad', '38 years')

# user_1.age = 40
user_1.age = '40'  # set
print(user_1.age)  # get
user_1.set_older()
print(user_1.age)
