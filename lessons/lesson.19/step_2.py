import pandas as pd

pupils = ['Антон', 'Игорь', 'Анна', 'Иван', 'Ольга', 'Сергей']
salary = [598.5, 1489.1, 3547.8, 1480.1, 6963.1, 8693.1]

pupils_s = pd.Series(salary, name='Salary', index=pupils)
pupils_s.index.name = 'Name'
# pupils_s.name = 'salary'
# print(pupils_s.index)
# print(pupils_s)
# print(pupils_s.values)
# print(pupils_s.keys())
# print(*pupils_s.items())
# print(pupils_s.values.sum())
# print(pupils_s.values.mean())
# print(pupils_s.values.std())
print(pupils_s['Антон':'Иван'])
# print(pupils_s['Антон':'Иван'].values.sum())
# print(pupils_s['Антон':'Иван'].agg('sum'))
# print(pupils_s['Антон':'Иван'].sum())
# print(pupils_s['Антон':'Иван'].max())
# print(pupils_s['Антон':'Иван'].min())
print(pupils_s['Антон':'Иван'].mean())
print(pupils_s['Антон':'Иван'].median())  # 50%
# print(pupils_s['Антон':'Иван'].std())
# [598.5, 1480.1, 1489.1, 3547.8, 6963.1]

