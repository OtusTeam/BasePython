import pandas as pd

pupils = ['Антон', 'Игорь', 'Анна', 'Иван', 'Ольга', 'Сергей']
salary = [598.5, 1489.1, 3547.8, 1489.1, 6963.1, 8693.1]
age = [24, 31, 19, 37, 24, 35]
hobby = ['футбол', 'лыжи', 'лыжи', 'теннис', 'сноуборд', 'футбол']

salary_s = pd.Series(salary, name='Salary', index=pupils)
salary_s.index.name = 'Name'
age_s = pd.Series(age, name='Age', index=pupils)
# print(salary_s)
# print(age_s)

# df = pd.DataFrame([salary_s, age_s])
# df = df.append(pd.Series(hobby, name='Hobby', index=pupils))
# df = df.transpose()
# print(df)
# df = df.transpose()
# print(df.head())
# print(df[df['Age'] >= 25])
# print(df['Age'] >= 25)
# print(df['Игорь':'Ольга'])

df = pd.DataFrame({
    'Salary': salary,
    'Age': age,
    'Hobby': hobby
}, index=pupils)
df.info()
# print(df.describe(include=['float64', 'int64', 'object']))
print(df.describe(include='all'))
