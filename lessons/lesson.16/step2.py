import requests


# print(requests.__version__)
url =  'https://httpbin.org/headers'
headers = {
    "User-Agent": "MyOtusAgent",
}

response = requests.get(url, headers=headers)


if response.status_code == 200:
    # print(response.text)
    print(response.content)