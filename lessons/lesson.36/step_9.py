import pandas as pd

df = pd.DataFrame({'country': ['Russia', 'Kazakhstan', 'Ukraine', 'Belarus'],
                   'population': [144.5, 18.3, 42.4, 9.5],
                   'square': [17_250_000, 2_724_900, 603_628, 207_595]},
                  index=['RU', 'KZ', 'UA', 'BY'])
df.index.name = 'code'
# print(df.describe(include='all'))
# df.info()

df['density'] = df.population / df.square * 1000000
df['density_int'] = df['density'].apply(lambda x: round(x))
# df = df.drop('density', axis=1)
# df.drop('density', axis=1, inplace=True)
df.drop(columns=['density'], inplace=True)
print(df)

df.to_csv('countries.csv')
df.to_json('countries.json')
df.to_pickle('countries.pickle')
