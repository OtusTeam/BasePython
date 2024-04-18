# O(n ** 2) -> cpu, memory
# O(n) -> cpu, memory
# O(n) = O(2 * n)
# leetcode.com

def to_upper(items):
    fruits_upper = []
    for el in items:
        fruits_upper.append(el.title())

    return fruits_upper  # n elements


fruits = ['apple', 'peach', 'lemon']

print(fruits)
result = to_upper(fruits)
print(result)
