import numpy as np

salary = np.array([15.5, 17.1, 16.8, 23.7, 7.1, 139.6, 1000])
salary.sort()
# salary_sorted = sorted(salary)
# print(type(salary), type(salary_sorted))
# print(salary_sorted)
print(salary)
print(salary.mean())
print(np.median(salary))
