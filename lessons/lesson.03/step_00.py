def hello(name):
    print("Hello,", name)
    if len(name) > 3:
        return len(name)
    print("Bye bye!")
    return "too short"


res = hello("John")
print(res)
res = hello("Sam")
print(res)
