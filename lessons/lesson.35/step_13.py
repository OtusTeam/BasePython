import numpy as np

salary = np.array([15.5, 17.1, 16.8, 23.7, 7.1, 139.6, 1000])
salary_diff = np.diff(salary)
top_workers_idxs = np.where(salary > 20)
top_workers = salary[top_workers_idxs]
print(top_workers_idxs)
print(top_workers)
print(salary_diff)

salary_std = np.sqrt(np.square(salary - salary.mean()).sum() / len(salary))
print(salary_std)
print(salary.std())
