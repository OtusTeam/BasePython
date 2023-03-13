def say_hello(user_name: str, greeting='', start_word='hello', **kwargs) -> None:
    # print(kwargs)
    # # validate = kwargs['validate']
    # validate = kwargs.get('validate', False)
    # print(validate)
    print(start_word, user_name, greeting)

    # return None


say_hello('a.andreeev')
print(say_hello('a.andreeev'))
# say_hello('a.andreeev', validate=False)
# say_hello('a.andreeev', greeting='jump', smth='go')

# SRP
