fruits = ['apple', 'peach', 'lemon']
phones = ['iPhone', 'Galaxy', 'Xiaomi']
tablets = ['iPad', 'Tab', 'Surface']
# apple, iPhone, iPad
# a, b = b, a
# for fruit, phone, tablet in zip(fruits, phones, tablets):
#     print(fruit, phone, tablet)

for row in zip(fruits, phones, tablets):
    # print(row)
    print(', '.join(row))
