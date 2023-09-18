class User:  # UpperCamelCase
    pass


user_1 = User()
user_2 = User()
user_3 = User()
print(type(user_1))
print(user_1, user_2, user_3)
print(vars(user_1))  # state == {'color': 'red', 'power': 100}
