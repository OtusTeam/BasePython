import numpy as np
import pandas as pd

# workers_salary_s = pd.read_pickle('data/workers_salary_s.pickle')
# print(workers_salary_s)

workers = ['Антон', 'Игорь', 'Анна', 'Иван', 'Николай']
worker_id = [num for num in range(1, len(workers) + 1)]
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1]
age = [27, 38, 24, 19, 43]

# workers = pd.read_csv()
workers = pd.DataFrame(np.transpose([worker_id, workers, salary, age]),
                       columns=['worker_id', 'name', 'salary', 'age'])
# workers = workers.set_index('worker_id')
workers.set_index('worker_id', inplace=True)
print(workers)
workers.reset_index(inplace=True)
print(workers)
