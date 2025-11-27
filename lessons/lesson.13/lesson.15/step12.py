import re



string = 'Мой контакт: Анна   anna@mail.ru Анна   anna@mail1.ru Анна   anna1@mail.ru'
my_pattern = r'\b[\w.-]+@[\w-]+\.\w+\b'


result = re.findall(my_pattern, string)
print(result)
