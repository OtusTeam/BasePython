import re


# pattern = r'cat'
# text = 'cat and dog'
# res = re.match(pattern, text)
#
# print(res)
#
# if res:
#     print(res.group())



# pattern = r'cat'
# text = '123 cat and  cat dog'
# res = re.search(pattern, text)
#
# print(res)
#
# if res:
#     print(res.group())


# pattern = r'cat'
# text = '123 cat and  cat dog'
# res = re.findall(pattern, text)
#
# print(res)

# . - любой символ
# \d - любая цифра 0-9

# pattern = r"(\+7)(.)(\d{3})(.)(\d{3})(.)(\d{2})(.)(\d{2})"
# text = 'Телефон: +7 999 888-77-55 Второй номер +7-909-808-37-35'
# res = re.findall(pattern, text)
#
# print(res)



pattern = r"\b[\w.-]+@[\w.-]+\.[\w.-]+\b"
text = 'Контакты: +7 999 888-77-55 email: <bob@mail.ru>'
res = re.search(pattern, text)

if res:
    print(res.group())