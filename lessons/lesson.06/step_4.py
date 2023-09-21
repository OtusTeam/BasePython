class AuthError(Exception):
    pass


def update_email_handler(request):
    return_code = 200
    msg = 'updated'
    if not request.user:
        raise AuthError

    try:
        ...
        if not request.user:
            raise AuthError
    # except Exception as e:
    #     return_code = 500
    #     msg = 'smth wrong with server'
    except (ValueError, ZeroDivisionError) as e:
        logger.exception('update_email_handler')
        return_code = 400
        msg = 'wrong email'
    except AuthError as e:
        logger.exception('update_email_handler')
        return_code = 401
        msg = 'wrong creds'
        raise
    except Exception as e:
        return_code = 500
        msg = 'smth wrong with server'

    return return_code, msg


try:
    return_code, msg = update_email_handler(request)
except Exception as e:
    print(e)
    exit(1)
