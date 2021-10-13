import pandas as pd

workers = ['Антон', 'Игорь', 'Анна', 'Иван', 'Николай']
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1]

# workers_salary = dict(zip(workers, salary))
# avg_salary = sum(workers_salary.values()) / len(workers_salary)
# print(workers_salary)
# print(avg_salary)
workers_salary_s = pd.Series(salary,
                             index=workers,
                             dtype='float64',
                             name='workers_salary')
workers_salary_s.index.name = 'u_name'
print(workers_salary_s)
print(workers_salary_s.mean())
print(workers_salary_s.median())
print(workers_salary_s.std())
print(workers_salary_s.value_counts(normalize=True))
print(workers_salary_s.describe())
