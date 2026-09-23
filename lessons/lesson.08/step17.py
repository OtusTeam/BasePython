import pickle


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


with open('data/employees.pkl', 'wb') as f:
    pickle.dump(employees, f)


with open('data/employees.pkl', 'rb') as f:
    loaded_employees = pickle.load(f)


print(loaded_employees)