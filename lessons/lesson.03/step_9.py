from functools import wraps


def is_staff_only(func):
    @wraps(func)
    def inner(user_id, *args, **kwargs):
        # """
        # inner
        # """
        print(f'# user_id: {user_id}')
        if user_id == 1:
            result = func(user_id)
            return result

    return inner


@is_staff_only
def get_user_data(user_id):
    """
    Get user data from db
    """
    return {'user_id': user_id,
            'name': 'Ivan'}


user_1 = get_user_data(1)
print(user_1)
print(get_user_data.__doc__)
# print(dir(get_user_data))
