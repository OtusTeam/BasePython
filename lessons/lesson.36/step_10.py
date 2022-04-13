import pandas as pd

df = pd.DataFrame({'country': ['Russia', 'Kazakhstan', 'Ukraine', 'Belarus'],
                   'population': [144.5, 18.3, 42.4, 9.5],
                   'square': [17_250_000, 2_724_900, 603_628, 207_595]},
                  index=['RU', 'KZ', 'UA', 'BY'])
df.index.name = 'code'

df['density'] = df.population / df.square * 1000000
# print(df)
# df['density_int'] = df['density'].apply(lambda x: round(x))
df['density_int'] = df['density'].apply(round)
print(df)
# df = df.drop('density', axis=1)
# # df.drop('density', axis=1, inplace=True)
# df.drop(columns=['density'], inplace=True)
# print(df)
