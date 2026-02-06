import requests
from pprint import pprint


# print(requests.__version__)
# url = 'https://google.com/'
url = 'https://openweathermap.org/'

response = requests.get(url)
print(type(response))
# print(response.status_code)
# if response.status_code == 200:
if response:
    print(response.content)
    pprint(response.headers)
    pprint(response.text)
else:
    print('NO')