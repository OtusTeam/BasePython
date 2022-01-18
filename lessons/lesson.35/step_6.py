import numpy as np

prices_np = np.array(
    [[156.5, 147.5, 367.1, 1576.4],
     [973.4, 559.3, 26.7, 17.9]]
).astype('float32')
print(len(prices_np),
      prices_np.shape,
      prices_np.ndim,
      prices_np.size,
      prices_np.itemsize, sep='\n')
