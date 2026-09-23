import json

json_str = """
{
    "department": "Research & Development",
    "employeeCount": 3,
    "isRemoteTeam": false,
    "members": [
        {
            "name": "Alice",
            "age": 29
        },
        {
            "name": "Bob",
            "age": 34
        },
        {
            "name": "Eve",
            "age": 25
        }
    ]
}
"""
print(type(json_str))
data = json.loads(json_str)
print(data)
print(type(data))