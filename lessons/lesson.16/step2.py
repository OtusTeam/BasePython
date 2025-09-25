import requests

# url = 'https://httpbin.org/get'
url = 'https://httpbin.org/headers'

headers = {'User-Agent': 'MyOtusAgent'}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)