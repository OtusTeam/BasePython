from sys import getsizeof
import numpy as np

prices = [156.5, 147.5, 367.1, 1576.4] * 100
prices_np = np.array(prices).astype('float32')
qty = [14, 7, 9, 256] * 100
qty_np = np.array(qty).astype('uint8')

print(getsizeof(prices), getsizeof(qty))
print(getsizeof(prices_np), getsizeof(qty_np))
# print(qty)
# print(qty_np)
