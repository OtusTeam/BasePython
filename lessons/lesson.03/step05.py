import time


password = '123'
# user_input = input('Введите пароль: ')
#
# while password != user_input:
#     print('Вход не выполнен')
#     user_input = input('Введите пароль: ')
#
# print('Вход выполнен')

is_running = True
while is_running:
    # time.sleep(1)
    print('Вход не выполнен')
    user_input = input('Введите пароль: ')
    if user_input == '12345':
        is_running = False
else:
    print('Я вышел по else')

print('Вход выполнен')