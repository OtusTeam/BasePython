import pandas as pd

workers_salary = [
    {'name': 'Иван', 'salary': 169.5, 'age': 19},
    {'name': 'Алиса', 'salary': 211.1, 'age': 21},
    {'name': 'Боб', 'salary': 169.5, 'age': 29},
    {'name': 'Иван', 'salary': 541.9, 'age': 37},
]
workers_salary_df = pd.DataFrame(workers_salary)
print(workers_salary_df)
# print(workers_salary_df.iloc[1])
# print(workers_salary_df.loc[1])
# print(workers_salary_df.loc[1:3])
# print(workers_salary_df.iloc[1:3])

print(workers_salary_df.loc[1:3, 'age'])
print(type(workers_salary_df.loc[1:3, 'age']))

print(workers_salary_df.loc[1:3, ['age']])
print(type(workers_salary_df.loc[1:3, ['age']]))
