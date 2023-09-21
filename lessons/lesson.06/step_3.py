def update_email_handler(request):
    return_code = 200
    msg = 'updated'
    try:
        ...
    except ValueError as e:
        return_code = 400
        msg = 'wrong email'

    return return_code, msg
