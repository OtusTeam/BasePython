import numpy as np

salary = [159.3, 563.7, 578.1, 248.3]

# salary_as_np = np.array(salary)
salary_as_np = np.array(salary, dtype='uint32')
# salary_as_np = np.array(salary, dtype='float32')
# salary_as_np = np.array(salary, dtype=np.float32)
print(salary_as_np.shape)
print(salary_as_np.itemsize)
print(salary_as_np.dtype)


