import requests
import json


# url = 'https://httpbin.org/post'
url = 'https://httpbin.org/status/400'
data = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    }

json_data = json.dumps(data)

# response = requests.post(url, data=data)
response = requests.get(url)
# response = requests.post(url, json=json_data)

print(response.status_code)
print(response.status_code)

# print(response.json())