import random

MAX_NUM = 10 ** 3


def get_nums(attempts=3, cond=lambda x: x < 15):
    nums = []
    try:
        for _ in range(attempts):
            while True:
                num = random.randint(1, MAX_NUM)
                if cond(num):
                    nums.append(num)
                    raise StopIteration
    except StopIteration:
        pass

    return nums


nums_1 = get_nums()
print(nums_1)
