nums = [1, 2, 3, 5, 7, 9, 10]

res = dict()
for i in nums:
    if i % 2 != 0:
        res[i] = i * i

print(res)


result = {i: i * i for i in nums if i % 2 != 0}
print(result)

