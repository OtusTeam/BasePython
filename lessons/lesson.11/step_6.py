from itertools import zip_longest

users = ['Ivan', 'Olga', 'Sergey']
salaries = [158, 693, ]

# for user, salary in zip(users, salaries):
for user, salary in zip_longest(users, salaries, fillvalue=15):
    print(user, salary)
