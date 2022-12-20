def my_func(smth_by_link):
    # smth_by_link = smth_by_link[:]  # memory O(n)
    smth_by_link.append("It's me!")
    return smth_by_link


some_list = ['one', 'two']
some_list_2 = my_func(some_list[:])
print(some_list)
print(some_list_2)
