import numpy as np

salary = np.array([15.5, 17.1, 16.8, 23.7, 7.1, 139.6, 1000])
salary_stat = np.percentile(salary,
                            (25, 50, 75))
# print(salary)
print(salary.mean())
print(np.median(salary))
print(salary_stat)
