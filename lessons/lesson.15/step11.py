import re



string = 'Мой контакт: Анна   <anna@mail.ru>'
my_pattern = r'([А-Яа-яA-Za-z]+)\s+<(.+?)>'


result = re.search(my_pattern, string)
if result:
    print(result.group())
    print()
    print(result.group(1))
    print(result.group(2))
