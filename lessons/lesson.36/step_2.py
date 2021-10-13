import pandas as pd

workers = ['Антон', 'Игорь', 'Анна', 'Иван', 'Николай']
# workers = ['Антон', 'Игорь', 'Анна', 'Иван']
# workers = ['Антон', 'Игорь', 'Анна', 'Иван', 'Игорь']
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1]
# salary = [598.5, 1489.1, 3547.8, 1489.1]

workers_salary_s = pd.Series(
    salary,
    index=workers,
    dtype='float64',
    name='workers_salary'
).set_flags(allows_duplicate_labels=False)
workers_salary_s.index.name = 'u_name'
# print(workers_salary_s['Игорь':'Иван'])
# print(workers_salary_s['Игорь'])
# print(workers_salary_s[['Игорь', 'Иван']])
print(workers_salary_s.iloc[0])
print(workers_salary_s.iloc[0:2])
print(workers_salary_s.iloc[[0, 2]])
print(workers_salary_s.loc[['Игорь', 'Иван']])

workers_salary_s.loc[['Игорь', 'Иван']] = 7893.4
print(workers_salary_s)
