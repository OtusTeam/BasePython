def condition(x):
    return x.startswith('p')


fruits = ['apple', 'peach', 'lemon']

print(fruits)
# fruits_gen = (el.title() for el in fruits if el.startswith('p'))
# fruits_gen = (
#     el
#     for el in fruits
#     if el.startswith('p')
# )
fruits_iter = filter(
    # lambda x: x.startswith('p'),
    condition,
    fruits,
)  # O(1) memory

for el in fruits_iter:
    print(el)
