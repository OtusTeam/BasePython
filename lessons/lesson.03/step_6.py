nums_qty = 10


# nums = (el for el in range(nums_qty))


def nums_gen(nums_qty):
    for el in range(nums_qty):
        yield el  # not return!!!
        # print('done')


nums = nums_gen(nums_qty)
print(nums)
# print(nums[5])
# print(nums[5:8])
# print(next(nums))
# print(next(nums))
# print(next(nums))
