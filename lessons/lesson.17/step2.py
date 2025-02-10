import requests

url = "https://jsonplaceholder.typicode.com/posts/"

response = requests.get(url)

print(response.status_code)
print(type(response))

my_json = response.json()

print(type(my_json))
print(my_json)