import numpy as np
import pandas as pd

# workers_salary_s = pd.read_pickle('data/workers_salary_s.pickle')
# print(workers_salary_s)

workers = ['Антон', 'Игорь', 'Анна', 'Иван', 'Николай']
# workers = [7, 8, 9, 11, 12]
worker_id = [num for num in range(1, len(workers) + 1)]
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1]
age = [27, 38, 24, 19, 43]

workers = pd.DataFrame(np.transpose([worker_id, workers, salary, age]),
                       columns=['worker_id', 'name', 'salary', 'age'])
workers['worker_id'] = workers['worker_id'].astype('uint32')
workers['age'] = workers['age'].astype('uint8')
workers.set_index('worker_id', inplace=True)

# old_workers = workers[workers['age'] >= 35]
# old_workers = workers[workers['age'] >= 35]['age']
# old_workers = workers[workers['age'] >= 35][['age', 'name']]
# old_workers = workers[workers['age'] >= 35]['age'].agg(['min', 'max'])
old_workers = workers[workers['age'] >= 35].agg(['min', 'max'])
print(old_workers, type(old_workers))
