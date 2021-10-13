import numpy as np
import pandas as pd

# workers_salary_s = pd.read_pickle('data/workers_salary_s.pickle')
# print(workers_salary_s)

workers = ['Антон', 'Игорь', 'Анна', 'Иван', 'Николай']
worker_id = [num for num in range(1, len(workers) + 1)]
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1]
age = [27, 38, 24, 19, 43]

# workers = pd.read_csv()
workers = pd.DataFrame(np.transpose([workers, salary, age]),
                       columns=['name', 'salary', 'age'])
workers.index = worker_id
print(workers)
