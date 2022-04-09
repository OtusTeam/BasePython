import numpy as np

products = [156.3, 478.1, 9853.7, 6571.2]
discount = 3  # %
discount = (100 - discount) / 100
# classic python
disc_products = [el * discount for el in products]
print(disc_products)

np_products = np.array(products)
np_disc_products = np_products * discount
print(np_disc_products)
# print(type(np_products))
# print(products)
# print(np_products)

