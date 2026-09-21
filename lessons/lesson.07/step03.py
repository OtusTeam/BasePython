# res = []
# for i in range(1, 8):
#     res.append(str(i * 2))
#
# print(res)
#
#
# result = [str(i * 2) for i in range(1, 8)]
# print(result)



nums = ['1', '2', '3', '5', '6', '7']


new_list = map(int, nums)
print(list(new_list))


res = []
for item in nums:
    res.append(int(item))
print(res)


result = [int(num) for num in nums]
print(result)