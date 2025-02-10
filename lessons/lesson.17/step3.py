import requests

url = "https://jsonplaceholder.typicode.com/posts/"

params = {
    "userId": 1,
}

response = requests.get(url, params=params)

print(response.status_code)

my_json = response.json()

print(type(my_json))
print(my_json[0].get("title"))