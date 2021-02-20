import pandas as pd

pupils = ['Антон', 'Игорь', 'Анна', 'Иван', 'Ольга', 'Сергей']
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1, 8693.1]

pupils_s = pd.Series(salary, name='Salary', index=pupils)
pupils_s.index.name = 'Name'
# print(pupils_s.unique())
# print(pupils_s.count())
# freq = 200 < freq < 2000
# print(pupils_s > 2000)
# print(pupils_s[pupils_s > 2000])
# print(pupils_s[pupils_s <= 2000] * 1.5)
# print(pupils_s.head(3))
# print(pupils_s.tail(3))
# print(pupils_s.describe())
# print(pupils_s.mean())
print(pupils_s['Игорь':'Ольга'])
pupils_s['Игорь':'Ольга'] = 3500
print(pupils_s['Игорь':'Ольга'])
print(pupils_s[['Игорь', 'Ольга']])
pupils_s[['Игорь', 'Ольга']] = 3700
print(pupils_s)

