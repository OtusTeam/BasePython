from collections import deque


q = deque()

q.append('Anna')
q.append('Bob')
q.append('Emy')

print(q)

first = q.popleft()
print(first)

print(q)


first = q.popleft()
print(first)

print(q)

