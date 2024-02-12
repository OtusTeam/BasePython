def user_info():
    return "John", 42, "john@example.com"


print(user_info())

res = user_info()
print(res[0])
print(res[1])
print(res[2])

# name, age, email = res
name, age, email = user_info()
print("Name:", name)
print("Age:", age)
print("email:", email)
