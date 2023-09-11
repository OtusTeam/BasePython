def is_staff_only(func):
    def inner(user_id, *args, **kwargs):
        print(f'# user_id: {user_id}')
        # some logic
        if user_id == 1:
            result = func(user_id)
            return result

    return inner
    # return func


@is_staff_only
def get_user_data(user_id):
    return {'user_id': user_id,
            'name': 'Ivan'}


@is_staff_only
def my_summ(*args):
    return sum(*args)


user_1 = get_user_data(2)
# user_1 = is_staff_only(get_user_data)(1)
# user_1 = inner(2)
print(user_1)


