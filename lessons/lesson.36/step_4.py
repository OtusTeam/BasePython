import pandas as pd

salary = [169.5, 211.1, 169.5, 157.3, 541.9]
workers = ['Иван', 'Алиса', 'Боб', 'Иван', 'Петр']
salary_s = pd.Series(salary,
                     index=workers,
                     name='salary',
                     dtype='float32')

# print(salary_s)
# print(salary_s.mean(), salary_s.median())
# Counter
# print(salary_s.value_counts())
# print(salary_s.value_counts(normalize=True))
# salary_s.name = 'SALARY'
# sorted()
# l_1.sort()
# print(salary_s.reset_index(inplace=True, drop=True))
# tmp = salary_s.reset_index()
print(salary_s.index)
# tmp = salary_s.reset_index(drop=True)
# tmp = salary_s.reset_index(drop=True, inplace=True)
# var_1 = list_1.append(5)
# print(type(tmp))
# print(tmp.index)
# print(tmp)
salary_s.reset_index(drop=True, inplace=True)
print(salary_s)



# def my_func(salary_s):
#     salary_s = salary_s.copy()


def my_func(salary_s=tuple()):
    pass
