result = (x for x in range(1, 101) if x % 2 == 0)
print(result)


res = []
for num in range(1, 101):
    if num % 2 == 0:
        res.append(num ** 2)

print(res)