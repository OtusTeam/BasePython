import pandas as pd

salary = [169.5, 211.1, 157.3, 171.5, 541.9]
workers = ['Иван', 'Алиса', 'Боб', 'Иван', 'Петр']
salary_s = pd.Series(salary,
                     index=workers,
                     name='salary')  #.set_flags(allows_duplicate_labels=False)
print(salary_s)
# print(salary_s[2])
# print(salary_s['Боб'])
# print(salary_s['Иван'])
# print(salary_s['Иван':'Петр'])
# print(salary_s[1:3])
# print(salary_s['Алиса':'Боб'])
print(salary_s.iloc[1:3])
print(salary_s.loc['Алиса':'Боб'])

