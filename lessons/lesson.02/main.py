# DRY - do not repeat yourself

print("Hello World!")

name = "John"
print("Hello", name)

name = None

print(None)
print(type(None))

if name is None:
    name = "Sam"

print("Hello", name)

name = None
if name is None:
    name = "Pete"

print("Hello", name)


# value = "123"
# value == "123"
# user_registered = False
# if user_registered is False:
#     pass

username = ""
[]
{}
set()
if not username:
    print("username not set", username)

if username is None:
    pass

username = ""
if not username:
    print("no username")

if username is False:
    pass

if username is None:
    pass
