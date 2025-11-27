import re



string = 'Мой номер телефона: +7-979-123-45-679. Код 0022'
my_pattern = r'(\+7)-(\d{3})-(\d{3})-(\d{2})-(\d{2})'


result = re.search(my_pattern, string)
if result:
    print(result.group())
    print()
    print(result.group(1))
    print(result.group(2))
