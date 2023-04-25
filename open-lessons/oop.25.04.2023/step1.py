class User:
    name = None
    username = None
    age = None


sam = User()
print("sam:", sam, sam.name, sam.age)
print("sam dict:", sam.__dict__)

john = User()
print(john, john.name, john.age)
print("john dict:", john.__dict__)

print("dict eq?", john.__dict__ == sam.__dict__)
print("dict same object?", john.__dict__ is sam.__dict__)
john.name = "John"
john.age = 42
print(john, john.name, john.age)
print(john.__dict__)

print("sam:", sam, sam.name, sam.age)

print("___")
print("sam dict:", sam.__dict__)
print("john dict:", john.__dict__)

print("sam username", sam.username)
print("john username", john.username)


print(User.__dict__)
User.username = "default-username"
print(User.__dict__)

print("sam username", sam.username)
print("john username", john.username)

print("sam dict:", sam.__dict__)
print("john dict:", john.__dict__)
