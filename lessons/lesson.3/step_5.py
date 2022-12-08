products = ['phone', '', 'tablet', 'notebook', 'watch']


def show_products(items):
    for item in items:  # creates iterator
        # next()
        print(item, end=', ')
        # StopIteration
    print()


products_f_2 = [item for item in products if item]
show_products(products_f_2)
show_products(products_f_2)

products_f_3 = filter(bool, products)
print(*products_f_3)
print(*products_f_3)
# print(products_f_3[2])
# print(type(products_f_3))
# print(dir(products_f_3))

