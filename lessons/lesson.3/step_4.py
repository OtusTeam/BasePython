products = ['phone', '', 'tablet', 'notebook', 'watch']


def show_products(items):
    for item in items:  # creates iterator
        # next()
        print(item, end=', ')
        # StopIteration
    print()


products_f = []
for item in products:
    if item:
        products_f.append(item)
show_products(products_f)

products_f_2 = [item for item in products if item]
show_products(products_f_2)

# map(), zip()
products_f_3 = filter(bool, products)  # memory O(1)
# show_products(products_f_3)
# lazy calcs
print(next(products_f_3))
print(next(products_f_3))
print(next(products_f_3))
print(next(products_f_3))
print(next(products_f_3))

