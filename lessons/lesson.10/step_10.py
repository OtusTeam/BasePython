from collections.abc import Iterator, Iterable

numbers = [1, 2, 3]

print(numbers)
for num in numbers:
    print(num)


print("isinstance(numbers, Iterable):", isinstance(numbers, Iterable))
print("isinstance(numbers, Iterator):", isinstance(numbers, Iterator))

number_iterator = iter(numbers)

print("isinstance(number_iterator, Iterable):", isinstance(number_iterator, Iterable))
print("isinstance(number_iterator, Iterator):", isinstance(number_iterator, Iterator))

print("next iter:", next(number_iterator))
for num in number_iterator:
    print(num)


class RangeIter(Iterator):
    def __init__(self, current: int, stop: int) -> None:
        self.current = current
        self.stop = stop

    def __next__(self) -> int:
        val = self.current
        self.current += 1
        if self.current > self.stop:
            raise StopIteration
        return val


class Range:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __iter__(self) -> RangeIter:
        return RangeIter(self.start, self.stop)


rng = Range(0, 10)
print("isinstance(rng, Iterable):", isinstance(rng, Iterable))
print("isinstance(rng, Iterator):", isinstance(rng, Iterator))

# rng_iter = iter(rng)
# print("some rng:", [next(rng_iter) for _ in range(20)])

for num in rng:
    print(num, end=" ")
print()
