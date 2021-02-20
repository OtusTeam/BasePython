import pandas as pd

df = pd.DataFrame({
    'country': ['Russia', 'Kazakhstan', 'Ukraine', 'Belarus'],
    'population': [144.5, 18.3, 42.4, 9.5],
    'square': [17_250_000, 2_724_900, 603_628, 207_595],
},
    index=['RU', 'KZ', 'UA', 'BY'],
)
df.index.name = 'code'
df['density'] = df.population / df.square * 1_000_000
# df = df.drop('density', axis=1, inplace=True)
df = df.drop('density', axis=1)
print(df)
# [1, 2, 3].sort()
# sorted([1, 2, 3])
df.to_csv('countries.csv')
df.to_json('countries.json')
df.to_pickle('countries.pickle')
