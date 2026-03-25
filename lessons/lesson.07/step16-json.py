import json


with open('data/employees.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)
print(data.get("department"))
print(type(data))
