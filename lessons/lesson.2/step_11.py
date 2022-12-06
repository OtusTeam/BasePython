def my_func(smth_by_link):
    # smth_by_link = []
    print(id(smth_by_link))
    smth_by_link.append("It's me!")


# some_list = ['one', 'two']
some_list = ('one', 'two')
print(id(some_list))
print(some_list)

my_func(some_list)  # obj id

print(some_list)
