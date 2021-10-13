import pandas as pd

workers = ['Антон', 'Игорь', 'Анна', 'Иван', 'Николай']
# workers = ['Антон', 'Игорь', 'Анна', 'Иван']
# workers = ['Антон', 'Игорь', 'Анна', 'Иван', 'Игорь']
salary = [598.5, 1489.1, 3547.8, 1217.6, 6963.1]
# salary = [598.5, 1489.1, 3547.8, 1489.1]

workers_salary_s = pd.Series(
    salary,
    index=workers,
    dtype='float64',
    name='workers_salary'
).set_flags(allows_duplicate_labels=False)
workers_salary_s.index.name = 'u_name'
# print(workers_salary_s.agg(['min', 'max', 'median']))

# high_salary_idx = workers_salary_s > 3000
# print(high_salary_idx)
# print(workers_salary_s[high_salary_idx])
# print(workers_salary_s[workers_salary_s > 3000])
# print(workers_salary_s[(workers_salary_s > 5000) |
#                        (workers_salary_s < 1000)])
print(workers_salary_s[(workers_salary_s >= 2000) &
                       (workers_salary_s <= 4000)])

workers_salary_s[(workers_salary_s > 5000) |
                 (workers_salary_s < 1000)] *= 0.9

print(workers_salary_s)
print(workers_salary_s.array, type(workers_salary_s.array))
print(workers_salary_s.to_numpy(), type(workers_salary_s.to_numpy()))

workers_salary_s.to_pickle('data/workers_salary_s.pickle')


