import numpy as np

# print(np.__version__)

prices = [156.5, 147.5, 367.1, 1576.4] * 10
prices_np = np.array(prices)
# print(type(prices_np),
#       prices_np.shape,
#       prices_np.dtype)

discount = 5

prices_upd = [el * (1 - discount / 100)
              for el in prices]
prices_np_upd = prices_np * (1 - discount / 100)
# print(prices)
# print(prices_upd)
print(prices_np_upd)  # __str__
print(list(prices_np_upd))  # __str__
