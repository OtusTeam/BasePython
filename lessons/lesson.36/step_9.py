import pandas as pd

salary = [169.5, 211.1, 169.5, 157.3, 541.9]
workers = ['Иван', 'Алиса', 'Боб', 'Ольга', 'Петр']
# workers_salary = dict(zip(workers, salary))
workers_salary = [
    {'name': 'Иван', 'salary': 169.5},
    {'name': 'Алиса', 'salary': 211.1},
    {'name': 'Боб', 'salary': 169.5},
]
workers_salary_df = pd.DataFrame(workers_salary)
print(workers_salary_df)
# workers_salary_df.to_csv('salary.csv')
# workers_salary_df.to_json('salary.json')
# workers_salary_df.to_excel('salary.xlsx')
print(workers_salary_df.to_dict())
print(workers_salary_df.to_dict('records'))
