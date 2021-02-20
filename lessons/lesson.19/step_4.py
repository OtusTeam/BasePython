import pandas as pd

pupils = ['Антон', 'Игорь', 'Анна', 'Иван', 'Ольга', 'Сергей']
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1, 8693.1]

pupils_s = pd.Series(salary, name='Salary', index=pupils)
print(pupils_s.array)
print(type(pupils_s.array))
print(pupils_s.to_numpy())
print(type(pupils_s.to_numpy()))
