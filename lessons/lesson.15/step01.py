# argparse
# python main.py 10 --file data.txt
# pip install requests --upgrade

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('age')
parser.add_argument('--lang', default='python', help='Язык программирования')
args = parser.parse_args()

# print(f'Привет, {args.name}.')
print(f'Привет, {args.name}. Тебе {args.age} лет')
print(f'Ты изучаешь, {args.lang}. ')
if args.lang == 'python':
    print('Молодец')
elif args.lang == 'java':
    print('Иди учи sprint')
else:
    print('Неизвестный язык')