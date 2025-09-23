from collections import Counter


# text = 'abracadabra'
# counts = Counter(text)
# print(counts)


# text = 'Занятие Python « Расширенные возможности Python встроенной библиотеки Python »'
words = [1, 2, 3, 1, 2, 1]
# words = text.split()
counter = Counter(words)
print(counter)
print(counter[3])