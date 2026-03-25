def calc_nums(calc, num1, num2=10, num3=100):
    if calc == '+':
        result = num1 + num2 + num3
        return result
        print(123)
    if calc == '-':
        result = num3 - num2 - num1
        return result
        print(456)
    else:
        result = None
        return result
    print(789)


res = calc_nums("-", 1)
print(res)


