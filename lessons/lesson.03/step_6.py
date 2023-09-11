# def print_user_data(name, user_params, **kwargs):
def print_user_data(name, age, address=None, gender=None, grade=None, **kwargs):
    print(f'*{name}*, **{age}**')
    print(kwargs)
    if gender is not None:
        print(f'gender is {gender}')


print_user_data('Ivan', 25, gender='F', department='devs')
