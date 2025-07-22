from collections import Counter


text = '/home/stanislav/PycharmProjects/OTUS_M3_1_2025_05/.venv/bin/python /home/stanislav/PycharmProjects/OTUS_M3_1_2025_05/step08.py '
counter = Counter(text)
print(counter)

top3 = counter.most_common(3)
print(top3)

print(counter['s'])