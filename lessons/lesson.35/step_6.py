import numpy as np

# products = [156.3, 478.1, 9853.7, 6571.2]
products = [
    [156.3, 478.1, 9853.7, 6571.2],
    [156.1, 475.1, 9854.7, 6576.2],
    [156.2, 477.1, 9850.7, 6574.2],
]
np_products = np.array(products, dtype='int64')
np_products_32 = np_products.astype('int32')
print(np_products.dtype)
print(np_products_32.dtype)
