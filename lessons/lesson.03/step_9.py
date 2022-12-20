products = ['phone', 'tablet', 'notebook', 'watch']

products_f_3 = filter(bool, products)
print(*products_f_3)

products_f_4 = (item for item in products if item)
print(type(products_f_4))
print(*products_f_4)


def get_user_greet(username, greeting='Hi'):
    return f'{greeting}, {username}!'


# def get_user_greet_as_gen(username, greeting='Hi'):
#     yield f'{greeting}, {username}!'

