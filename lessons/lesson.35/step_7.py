import numpy as np

# products = [156.3, 478.1, 9853.7, 6571.2]
products = [
    [156.3, 478.1, 9853.7, 6571.2],
    [156.1, 475.1, 9854.7, 6576.2],
    [156.2, 477.1, 9850.7, 6574.2],
]
np_products = np.array(products, dtype='int64')
print(np_products.sum())
print(np_products.sum(axis=0))  # 3 or 4?
print(np_products.sum(axis=1))
