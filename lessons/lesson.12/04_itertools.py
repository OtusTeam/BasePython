from itertools import count, repeat, chain, combinations

users = [
    "Bob",
    "John",
    "Alice",
    "Kyle",
    "Leo",
]

for user, c in zip(users, count(start=1, step=4)):
    print(c, user)


my_numbers = [1, 3, 4, 5, 7, 8]

print(pow(2, 4))

for n in my_numbers:
    print(n, n**2)


print(list(map(pow, my_numbers, repeat(3))))

names_male = ["Bob", "Kyle", "Leo"]
names_female = ["Alice", "Sam", "Kate"]

all_names = names_male + names_female
# print(all_names)
all_data = [names_male, names_female]
print(all_data)

print(list(chain.from_iterable(all_data)))
print(list(chain(*all_data)))

for pair in combinations(all_names, 2):
    print(pair)
