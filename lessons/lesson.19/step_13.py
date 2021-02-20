import json

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1900)

pd.set_option('precision', 2)
f_name = 'fines.json'

with open(f_name, encoding='utf-8') as f:
    data = json.load(f)

values = data.get('Value')
_fines = json.loads(values).get('Fines')
# pprint(_fines[0])
fines = [
    {'Name': fine['ApnDetail'][0]['Value'].replace('\t', ' - '),
     'Place': fine['ApnDetail'][3]['Value'],
     'Fine sum': fine['FineSum'], }
    for fine in _fines
]

df = pd.DataFrame(fines)
# print(df.head())
summary = df.groupby('Name')['Fine sum'].agg(['count', 'sum']).sort_values(['count'], ascending=False)
print(summary)
# print(type(summary))
#
total = pd.Series(summary.sum(), name='Full summary')
# print(total)
summary = summary.append(total)
print(summary)
