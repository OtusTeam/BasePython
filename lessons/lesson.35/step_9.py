import numpy as np


salary = [579, 470, 193, 328, 478, 236, 697]
print(sorted(salary))
salary_as_np = np.array(salary)
print(salary_as_np.mean())
print(np.median(salary_as_np))

percents = (1, 5, 10, 25, 50, 75, 95, 99)
# percents = (25, 50, 75)
salary_stat = np.percentile(salary_as_np, percents)
print(salary_stat)
print(dict(zip(percents, salary_stat)))