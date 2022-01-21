import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1900)
pd.set_option('display.max_colwidth', 40)
pd.set_option('precision', 1)
# pd.set_option('max_info_columns', 3)
f_name = 'data/titanic.csv'
df = pd.read_csv(f_name)
print(df)
# print(df.to_dict('records'))
# print(df.head(3))
# print(df.tail(3))
# df.info()
# print(df.describe())

# print(df.columns)
# print(df['PClass'].value_counts())
# print(df.value_counts('PClass', normalize=True))
# print(df['Sex'].value_counts())
# print(df['Age'].value_counts())
# print(df.groupby('Sex'))
# print(df.groupby('Sex').count())
# print(df.groupby(['Sex', 'Survived']).count())
# print(df.groupby(['Sex', 'Survived'])['Age'].median())
# print(df.groupby(['Sex', 'Survived'])['PassengerID'].count())
# print(df.groupby(['Sex', 'Survived'])['Age'].std())
# print(df.groupby(['Sex', 'Survived'])['Age'].mean())
# print(df.groupby('Sex').median())
# print(df.groupby('Sex')['Age'].median())
# print(df.groupby('Sex')['Age'].max())
# print(df.groupby('Sex')['Age'].min())
# print(df.groupby('Sex')['Age'].mean())

# pivot = df.pivot_table(index=['Sex'],
#                        columns=['PClass'],
#                        values=['Age'],
#                        aggfunc='median')
# pivot = df.pivot_table(index=['Sex'],
#                        columns=['Survived'],
#                        values=['PassengerID'],
#                        aggfunc='count')
# pivot = df.pivot_table(index=['Sex'], columns=['Survived'], values=['Age'], aggfunc='mean')
# # pivot = df.pivot_table(index=['Sex'],
# #                        columns=['Survived'],
# #                        values=['Age'],
# #                        aggfunc='median')
# print(pivot)
