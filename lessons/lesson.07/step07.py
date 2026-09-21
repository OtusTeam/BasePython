res = []
for item in range(1, 21):
    if item % 5 != 0:
        if item % 2 == 0:
            res.append(item * 100)
        else:
            res.append(item + 10)
print(res)


result = [item * 100 if item % 2 == 0 else item + 10 for item in range(1, 21) if item % 5 != 0]
print(result)
