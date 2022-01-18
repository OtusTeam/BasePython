import numpy as np
from numpy.linalg import det

# prices = [[2, 4, 6, 8],
#           [3, 5, 7, 9],
#           [4, 6, 8, 10]]
prices = [[2, 4, 6],
          [3, 5, 7],
          [7, 6, 9]]
prices_np = np.array(prices)
# print(prices_np.sum())
# print(prices_np.sum(axis=0))
# print(prices_np.sum(axis=1))
# print(prices_np.prod())
# print(prices_np.prod(axis=0))
# print(prices_np.prod(axis=1))
prices_det = det(prices_np)
print(prices_det)
