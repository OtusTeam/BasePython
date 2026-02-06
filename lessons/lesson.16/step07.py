import requests


url = "https://httpbin.org/post"

data = {
    'user_name': "Bob",
    'user_age': 32,
}

response = requests.post(url, data=data)
# response = requests.post(url, json=json)

print(response.status_code)
if response:
    print(response.headers)
    print(response.text)
else:
    print('NO')