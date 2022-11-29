user_name = 'Ivan'
user_name_adv = user_name.replace('I', 'i')
print(id(user_name), id(user_name_adv))
print(user_name is user_name_adv)

