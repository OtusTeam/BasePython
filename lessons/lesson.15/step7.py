import re

#
result = re.match(r'cat', '111cat  catand dog')
if result:
    print(f' match {result.group()}')


result = re.search(r'cat', '11ca  and dog')
if result:
    print(f' search {result.group()}')
# print(result)


result = re.findall(r'ca12t', '11cat  ancatd dcatog')
if result:
    print(f' search {result}')
# print(result)

text = 'Мой номер 123 - 45 еще 7894-asd !'
result = re.findall(r'\d+', text)
if result:
    print(f' search {result}')

# . - любой символ
# \d - любая цифра
# \w - любая буква
# \s -любой пробельный символ


text = 'Мой номер Один два три Боб-45 еще 7894-asd !'
result = re.findall(r'\b[А-Я][а-я]+\b', text)
if result:
    print(f' search {result}')


text = 'Телефон: +7-987-123-45-67'
result = re.search(r'(\+7)-(\d{3})-(\d{3})-(\d{2})-(\d{2})', text)
if result:
    print(f' Тел {result.group(0)}')
    print(f' Тел {result.group(1)}')
    print(f' Тел {result.group(2)}')
    print(f' Тел {result.group(3)}')
    print(f' Тел {result.group(4)}')
    print(f' Тел {result.group(5)}')


text = 'Телефон: +7-987-123-45-67, +7-487-323-35-65'
result = re.findall(r'(\+7)-(\d{3})-(\d{3})-(\d{2})-(\d{2})', text)
if result:
    print(f' Тел {result}')


