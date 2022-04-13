import pandas as pd

salary = [169.5, 211.1, 157.3, 169.5, 541.9]
workers = ['Иван', 'Алиса', 'Боб', 'Иван', 'Петр']
salary_s = pd.Series(salary,
                     index=workers,
                     name='salary')
# salary_s.name = 'Salary'
print(salary_s)
# print(salary_s[2])
print(salary_s.index)
