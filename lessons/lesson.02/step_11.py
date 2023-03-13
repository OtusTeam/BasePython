users = ['i.ivanov', 'a.andreeev', 's.sergeev']
to_say = 'hi'

# greetings = []
# for user in users:
#     if not user.startswith('a'):
#         greetings.append(f'{user}, {to_say}!')  # f-strings

greetings = [f'{user}, {to_say}!'
             for user in users
             if not user.startswith('a')]

# greetings = [f'{user}, {to_say}!' for user in users if not user.startswith('a')]

print(greetings)

# filter(), map(), zip()
