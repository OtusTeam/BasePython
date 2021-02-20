import pandas as pd

pupils = ['Антон', 'Игорь', 'Анна', 'Иван', 'Ольга', 'Сергей']
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1, 8693.1]
age = [24, 31, 19, 37, 24, 35]
hobby = ['футбол', 'лыжи', 'лыжи', 'теннис', 'сноуборд', 'футбол']

df = pd.DataFrame([salary, age, hobby], index=['Salary', 'Age', 'Hobby'], columns=pupils)
df = df.transpose()
# 'Salary', 'Age', 'Hobby'
df.info()
# print(df.describe(include=['float64', 'int64', 'object']))
print(df.describe(include='all'))
print(df.head(3))
