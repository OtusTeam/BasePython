import pandas as pd

salary = [169.5, 211.1, 157.3, 169.5, 541.9]
salary_s = pd.Series(salary)
print(type(salary_s))
print(salary_s)
# print(dir(salary_s))
print(salary_s.to_list())
print(salary_s.to_numpy().nbytes)
