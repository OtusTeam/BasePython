import pandas as pd

salary = [169.5, 211.1, 169.5, 157.3, 541.9]
workers = ['Иван', 'Алиса', 'Боб', 'Ольга', 'Петр']

workers_salary = [
    {'name': 'Иван', 'salary': 169.5, 'age': 19},
    {'name': 'Алиса', 'salary': 211.1, 'age': 21},
    {'name': 'Боб', 'salary': 169.5, 'age': 29},
    {'name': 'Иван', 'salary': 541.9, 'age': 37},
]
workers_salary_df = pd.DataFrame(workers_salary)
# print(workers_salary_df)
workers_salary_df.set_index('name', inplace=True)
# print(workers_salary_df)

# for row in workers_salary_df:
# for row in workers_salary_df.values:
# for row in workers_salary_df.iterrows():
for idx, row in workers_salary_df.iterrows():
    print(idx)
    # print(type(row))
    # print(row['age'])
    # print(row.age)
    print(row.salary)
    print('-' * 25)
