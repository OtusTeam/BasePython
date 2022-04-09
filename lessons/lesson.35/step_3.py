from sys import getsizeof

import numpy as np

# products = [156.3, 478.1, 9853.7, 6571.2]
products = [
    [156.3, 478.1, 9853.7, 6571.2],
    [156.1, 475.1, 9854.7, 6576.2],
    [156.2, 477.1, 9850.7, 6574.2],
]
# products = [156, 478, 9853, 6571]
np_products = np.array(products, dtype='int64')
print(np_products.dtype)
print(np_products.ndim)
print(np_products.size)
print(np_products.shape)
print(np_products.itemsize)

print(getsizeof(products))
print(getsizeof(np_products))

