def get_user_data(user_id=None):
    name = 'Ivan'
    age = 25
    address = 'Moscow'
    gender = 'F'
    grade = 'Junior'
    return name, age, address, gender, grade


# a, b = b, a
# a, b, c = c, a, b
# user_name, age = get_user_data()
user_name, age, *trash = get_user_data()
print(user_name, age)
print(trash)

user_name, user_age, user_address, *trash = get_user_data()
print(user_name, user_age, user_address)
print(trash)
