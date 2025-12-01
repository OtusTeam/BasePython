import requests

url = 'http://127.0.0.1:8083/about_us'
data = {
    'name': 'Bob',
    'age': 21,
    'email': 'bob@gmail.com'
}
# response = requests.get(url)
response = requests.post(url, data=data)

print(response.status_code)
print(response.text)