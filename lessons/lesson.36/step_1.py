import pandas as pd

salary = [169.5, 211.1, 157.3, 169.5, 541.9]
salary_s = pd.Series(salary)
# print(salary_s.tolist())
# print(salary_s.to_numpy())
print(salary_s.describe())
