from collections import deque

queue = deque()

queue.append('Боб')
queue.append('Иван')
queue.append('Анна')

print(queue)
print(type(queue))

first = queue.popleft()
print(queue)
print(first)

queue.appendleft('Мэри')
print(queue)

last = queue.pop()
print(queue)
print(last)