fruits = ['apple', 'peach', 'lemon']
for _ in range(3):
    for fruit in fruits:
        if fruit == 'apple':
            continue
        print('this is', fruit)  # next(...) -> StopIteration
        if fruit == 'peach':
            break

for fruit in fruits:
    if fruit == 'apple':
        continue

    print('this is', fruit)  # next(...) -> StopIteration
    if fruit == 'peach':
        break

