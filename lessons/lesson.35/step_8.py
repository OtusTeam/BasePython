import numpy as np

# products = [156.3, 478.1, 9853.7, 6571.2]
products = [[[156.3],
             [156.1]],
            [[156.3],
             [156.1]],
            [[156.3],
             [156.1]]]
np_products = np.array(products, dtype='int64')
print(np_products.sum())
print(np_products.sum(axis=0))  # 3 or 4?
print(np_products.sum(axis=1))
print(np_products.ndim)
print(np_products.shape)
# (1080, 1920, 3)
