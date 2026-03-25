import json


employees = {
    "department": "Research & Development",
    "employeeCount": 3,
    "isRemoteTeam": False,
    "members": [
        {"name": "Alice", "age": 29},
        {"name": "Bob",   "age": 34},
        {"name": "Eve",   "age": 25}
    ]
}

json_str = json.dumps(employees)

print(json_str)
print(type(json_str))


inc_json = json_str
data = json.loads(inc_json)
print(data)
print(data.get("department"))
print(type(data))
