import numpy as np

salary = [159.3, 563.7, 578.1, 248.3]

salary_as_np = np.array(salary)

# print(type(salary_as_np))
# print(salary)
# print(salary_as_np)

scale = 1.05
salary_upd = salary_as_np * scale
print(salary_upd)
print(np.round(salary_upd, 2))
print(list(np.round(salary_upd, 2)))

