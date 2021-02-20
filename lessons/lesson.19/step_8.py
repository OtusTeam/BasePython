import pandas as pd

pupils = ['Антон', 'Игорь', 'Анна', 'Иван', 'Ольга', 'Сергей']
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1, 8693.1]
age = [24, 31, 19, 37, 24, 35]
hobby = ['футбол', 'лыжи', 'лыжи', 'теннис', 'сноуборд', 'футбол']

df = pd.DataFrame({
    'Salary': salary,
    'Age': age,
    'Hobby': hobby
}, index=pupils)

# print(df['Антон':'Иван']['Age'])
# print(df['Антон':'Иван'][['Age', 'Salary']])
# print(df['Антон':'Иван'][['Age', 'Salary']].count())
# print(df['Антон':'Иван'][['Age', 'Salary']].sum())
print(type(df['Антон':'Иван']['Age']))
print(df['Антон':'Иван']['Age'].dtype)
print(df.Age)
df.info()
df.Age = df.Age.astype('int32')
print(df['Антон':'Иван']['Age'].dtype)
df.info()
