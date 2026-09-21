res = []
for item in range(1, 21):
    if item % 2 == 0:
        res.append(str(item))
print(res)


result = [str(item) for item in range(1, 21) if item % 2 == 0]
print(result)
print(type(result))