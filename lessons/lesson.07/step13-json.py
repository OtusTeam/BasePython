# {
#     "country": "Finland",
#     "capital": ["Helsinki", "Helsinki"],
#     "population": 5600000,
#     "isNordic": true,
#     "country1": {
#                     "country": "Finland",
#                     "capital": ["Helsinki", "Helsinki"],
#                     "population": 5600000,
#                     "isNordic": true,
#                     "country1": "Finland",
#                 },
# }

import json


json.dumps(obj)
json.dump(obj, file)
json.loads(s)
json.load(file)
