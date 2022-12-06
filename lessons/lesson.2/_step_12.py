def my_func(smth_by_value):
    # global some_val
    # some_val = 'change'
    print(id(smth_by_value))
    print(smth_by_value)


some_val = 'jump',
print(id(some_val))
print(some_val)

my_func(some_val)

print(some_val)
