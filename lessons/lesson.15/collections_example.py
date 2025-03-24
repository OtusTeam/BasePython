from collections import namedtuple, defaultdict, Counter, deque

# namedtuple
Person = namedtuple("Person", ['name', 'age'])

john = Person("John Doe", 27)

print(f'{john.name=}\n{john.age=}')

# Стандартный словарь
standart = dict()
if 'counter' not in standart:
    standart['counter'] = 0
else:
    standart['counter'] += 1
print(standart)

# Defaultdict
d = defaultdict(list)
d['counter'].extend(['2025-03-25 12:11:11.12321312'])
print(dict(d))

text = 'cat cat dog dog dog dog fly fly bug bug bug bug'.split(' ')

c = Counter(text)
print('-'*20, '\n', dict(c))

# Стандартный список

l = list()
l.insert(0, 'first')
l.append('second')
l.insert(0, 'zero')
print(f'{l=}')
l.pop(0)
l.pop(-1)
print(f'{l=}')


# Двусторонние очереди

def first():
    print('first')

def win():
    print('win')

def bug():
    print('bug')


tasks = deque()

tasks.appendleft(first)
tasks.appendleft(win)
tasks.appendleft(bug)

task = tasks.pop()
task()
task = tasks.pop()
task()
task = tasks.pop()
task()