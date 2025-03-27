import requests

url = "https://randomfox.ca/floof"
result = requests.get(url)

print(type(result))
if result:
    print("Success")
    my_img = result.json().get('link')
    print(my_img)