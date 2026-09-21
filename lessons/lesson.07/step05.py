a = [1, 2, 3]
b = [10, 20, 30]

res = []
for x in a:
    for y in b:
        if y != 20:
            res.append(str(x + y))
print(res)


result = [str(x + y) for x in a for y in b if y != 20]
print(result)