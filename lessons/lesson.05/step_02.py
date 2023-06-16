# class User(object):
class User:
    foo = "bar"
    # age =


print(User)
print(User.__dict__)
print(User.mro())

sam = User()
print("sam dict", sam.__dict__)
sam.username = "sam"
print("sam dict 2", sam.__dict__)
sam.age = 19
print("sam dict 3", sam.__dict__)

print(sam)
print(sam.username)
print(sam.age)

john = User()
john.username = "john"

print(john)
print(john.username)
print(john.__dict__)
print(john.foo)
john.foo = "spameggs"
print(john.__dict__)

print(john.foo)
User.foo = "fizzbuzz"
print(john.foo)
# print(john.age)
