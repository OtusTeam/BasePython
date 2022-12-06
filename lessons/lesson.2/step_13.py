# def split_nums(nums):
#     return nums.split(',')


def split_nums(nums):
    a, b = nums.split(',')
    return a, b
    # return {'a': a,
    #         'b': b}


nums = split_nums('1,2')
print(nums)
