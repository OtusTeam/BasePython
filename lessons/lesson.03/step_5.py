def print_user_data(name, age, address=None, gender=None, grade=None):
    print(f'*{name}*, **{age}**')
    # print(address, gender, grade)
    if gender is not None:  # gender = '', gender = None
    # if gender:  # gender = '', gender = None
        print(f'gender is {gender}')


# print_user_data('Ivan', 25, 'Moscow')
# print_user_data('Ivan', 25, None, 'F', None)
# print_user_data('Ivan', 25, gender='F')
print_user_data('Ivan', 25, gender='')
