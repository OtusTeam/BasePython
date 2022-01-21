import pandas as pd

salary = [169.5, 211.1, 169.5, 157.3, 541.9]
workers = ['Иван', 'Алиса', 'Боб', 'Иван', 'Петр']
salary_s = pd.Series(salary,
                     index=workers,
                     name='salary',
                     dtype='float32')

# print(salary_s)
# print(salary_s.mean(), salary_s.median())
# print(salary_s.value_counts())
# print(salary_s.value_counts(normalize=True))
salary_s.name = 'SALARY'
# print(salary_s.reset_index(inplace=True, drop=True))
# salary_s = salary_s.reset_index()
salary_s.reset_index(inplace=True, drop=True)
# salary_s = salary_s.reset_index(drop=True)
print(salary_s)
print(type(salary_s))

# some_list.sort() VS sorted()
