from collections import deque
from itertools import chain

names_male = ["Pete", "John", "Nick"]
names_female = ["Kate", "Alice"]
names_lists = [names_male, names_female]

names = list(chain.from_iterable(names_lists))
# names = list(chain(*names_lists))


def demo_deque():
    # queue = deque(tuple(names_male))
    queue = deque()
    # for name in names_male:
    #     queue.append(name)
    queue.extend(names_male)
    # FIFO = Fist In, First Out
    print(queue)
    print(queue.popleft())
    print(queue)
    print(queue.popleft())
    print(queue)
    queue.append("Kate")
    queue.append("Alice")
    print(queue)
    print(queue.popleft())
    print(queue)
    print(queue.popleft())
    print(queue)


def main():
    demo_deque()


if __name__ == '__main__':
    main()

