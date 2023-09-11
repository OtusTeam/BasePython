def print_user_data(name, age, *args):
    print(f'*{name}*, **{age}**')
    print(args)


# print_user_data('Ivan')
# print_user_data('Ivan', 25)
print_user_data('Ivan', 25, 'Moscow')
# name, age, *args = 'Ivan', 25, 'Moscow'
# calc_total(item_1, item_2)
