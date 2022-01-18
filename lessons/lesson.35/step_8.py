import numpy as np

# zero_1 = np.zeros((8, 1))
# zero_1 = np.empty((8, 1))
prices = [[156.5, 147.5, 367.1, 1576.4],
          [973.4, 559.3, 26.7, 17.9]]
prices_np = np.array(prices)
print(prices_np)
prices_np_reshaped = prices_np.transpose()
print(prices_np_reshaped)
# print(zero_1)
