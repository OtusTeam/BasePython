def set_older(user):
    # add validation
    user['age'] += 1

    return user


user_1 = {
    'name': 'Ivan',
    # 'age': '25',
    'age': '25 years',
    'address': None,
}
print(user_1['age'])
user_1 = set_older(user_1)
print(user_1['name'])
print(user_1['age'])

user_2 = {
    'name': 'Boris',
    'age': 30,
    'address': 'Moscow',
}
print(user_2['age'])
user_2 = set_older(user_2)
print(user_2['name'])
print(user_2['age'])
