import random

MAX_NUM = 10 ** 3


def get_nums(attempts=3, cond=lambda x: x < 15):
    nums = []
    is_ok = False
    for _ in range(attempts):
        while True:
            num = random.randint(1, MAX_NUM)
            if cond(num):
                is_ok = True
                break
        nums.append(num)
        if is_ok:
            break
    return nums


nums_1 = get_nums()
print(nums_1)
