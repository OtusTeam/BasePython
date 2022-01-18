import numpy as np

prices = [[156.5, 147.5, 367.1, 1576.4],
          [973.4, 559.3, 26.7, 17.9]]
prices_np = np.array(prices)
print(prices_np.shape, prices_np.ndim)
# print(prices)
print(prices_np)
# prices_np_reshaped = prices_np.reshape((3, -1))
# prices_np_reshaped = prices_np.reshape((4, -1))
# prices_np_reshaped = prices_np.reshape((8, -1))
prices_np_reshaped = prices_np.reshape((8,))
# prices_np_reshaped = prices_np.reshape((4, 2))
print(prices_np_reshaped)
print(prices_np_reshaped.shape, prices_np_reshaped.ndim)
