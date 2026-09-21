nums = [1, 2, 3, 2, 1, 5, 7, 5, 3, 9, 10]

res = set()
for i in nums:
    if i % 2 != 0:
        res.add(i)

print(res)


result = {i for i in nums if i % 2 != 0}
print(result)
