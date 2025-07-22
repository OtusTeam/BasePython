# d = {}
# d['a'] += 1

from collections import defaultdict


d = defaultdict(int) # list, set, str
d['a'] += 1
d['b'] += 2
d['c'] += 3

print(d)