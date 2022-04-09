products = [156.3, 478.1, 9853.7, 6571.2]
discount = 3  # %
discount = (100 - discount) / 100
# disc_product = products[0] * discount
# disc_products = products * discount
# imperative VS declarative
# GIL
disc_products = [el * discount for el in products]
print(disc_products)
