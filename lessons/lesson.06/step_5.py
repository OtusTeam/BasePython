class AuthError(Exception):
    pass


def update_email_handler(request):
    return_code = 200
    msg = 'updated'
    try:
        ...
    # except Exception as e:
    #     return_code = 500
    #     msg = 'smth wrong with server'
    except (ValueError, AuthError) as e:
        print(e.args)
        return_code = 400
        msg = 'validation error'
    except Exception as e:
        return_code = 500
        msg = 'smth wrong with server'

    return return_code, msg
