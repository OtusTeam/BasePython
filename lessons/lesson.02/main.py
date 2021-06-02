# DRY - do not repeat yourself

name = None

if name is None:
    name = "World!"
print("Hello", name)


# set default name to None
name = None

if name is None:
    name = "World"
print("Hello", name)


name = "Sam"

if name is None:
    name = "World"
print("Hello", name)

