my_list2 = ['anna', 'bob', 'alice', 'carol', 'John', ['bob', 'bob', 'bob', 'bob']]
for i in range(len(my_list2[5]) - 1, -1, -1):
    if my_list2[5][i] == 'bob':
        my_list2[5].pop(i)
print(my_list2)
print(my_list2[5].count('bob'))