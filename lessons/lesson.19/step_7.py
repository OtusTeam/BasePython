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
# df.info()
# print(df.describe(include='all'))

# print(df)
print(df.loc['Антон'])
print(df.loc['Антон':'Иван'])
print(df['Антон':'Иван'])
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[1:3])
