import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1900)
# pd.set_option('precision', 2)

f_name = 'data/weights.csv'
# df = pd.read_csv(f_name, index_col=0)
df = pd.read_csv(f_name,
                 index_col=0,
                 parse_dates=True)
print(df)
# print(df.head())
df.info()
# print(df.describe(include='all'))
# print(df.sort_index(ascending=True))
# print(df['US0527691069 US'].head())
# print(df['US0527691069 US'])
# print(df.agg(['min', 'max', 'mean', 'median']))
print(df.idxmax())
print(df.idxmin())
# print(df.nunique())
print(df.loc[df.idxmax()])
print(df.loc[df.idxmin()])

