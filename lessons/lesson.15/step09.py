import re


text = "Пишите на ivan@mail.ru и maria@gmail.com, gates@microsoft.gov.ru а также bob@yandex.net!"

# pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"
pattern = r"\b[\w.-]+@[\w.-]+\...\b"

emails = re.findall(pattern, text)
print(f'Найденные email: {emails}')
