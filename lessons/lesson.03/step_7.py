from time import sleep


def is_staff_only(func):
    def inner(user_id):
        print(f'# user_id: {user_id}')
        # go to db
        if user_id == 1:
            result = func(user_id)
            return result

    return inner


# @log_sentry
# @inject_trace_id
# @is_superadmin_only
@is_staff_only
def get_user_data(user_id):
    # if not user.is_staff:
    #     return
    sleep(0.5)
    return {'user_id': user_id,
            'name': 'Ivan'}


user_1 = get_user_data(2)
print(user_1)
