import pandas as pd

pupils = ['Антон', 'Игорь', 'Анна', 'Иван', 'Юлия']
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1]

pupils_s = pd.Series(salary, name='Salary', index=pupils)
# pupils_s.name = 'salary'
pupils_s.index.name = 'Name'
print(pupils_s)
print(pupils_s.index)
