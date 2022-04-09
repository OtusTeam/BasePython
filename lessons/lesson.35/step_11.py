import numpy as np

# np_prod = np.empty((5, 100))
# np_prod = np.zeros((5, 100))
# print(np_prod)

np_products = np.array([156.3, 478.1, 9853.7, 6571.2, 3605.7])
products = np.array(['apple', 'lime', 'water', 'bread', 'butter'])
cheap_prod_idx = np_products < 1000
# print(cheap_prod_idx)
# print(cheap_prod_idx.sum())
# cheap_prod = np_products[cheap_prod_idx]
# cheap_prod = np_products[np_products < 1000]
# cheap_prod = products[cheap_prod_idx]
# cheap_prod_price = np_products[cheap_prod_idx]
# print(cheap_prod, cheap_prod_price.sum())
# np.where()

# image_dark = image <= 5
# image[image_dark] += 5
np_products[cheap_prod_idx] *= 1.2
print(np_products)
