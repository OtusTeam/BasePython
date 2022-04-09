import numpy as np

np_products = np.array([156.3, 478.1, 9853.7, 6571.2, 3605.7, 7896547.2, 0.5])
# np_products = np.array([156.3, 478.1, 9853.7, 6571.2])
# median(), mean(), avg()
print(np_products.mean())
# print(np.mean(np_products))
print(np.median(np_products))
print(np.sort(np_products))
