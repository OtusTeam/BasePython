import numpy as np
import pandas as pd

w_data = [
    [169.5, 211.1, 169.5, 157.3, 541.9],
    [19, 34, 22, 26, 37],
]
w_data = np.array(w_data).transpose()

workers = ['Иван', 'Алиса', 'Боб', 'Ольга', 'Петр']

workers_salary_df = pd.DataFrame(w_data,
                                 index=workers,
                                 columns=['salary', 'age'])
print(workers_salary_df)
workers_salary_df.info()

