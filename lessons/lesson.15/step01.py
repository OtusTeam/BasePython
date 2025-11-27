import argparse


parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('age')
parser.add_argument("--lang", default='ru', help='Язык приветствия. ru -  по умолчанию')

args = parser.parse_args()

if args.lang == 'ru':
    print(f'Привет, {args.name}. Тебе {args.age} лет')
elif args.lang == 'en':
    print(f'Hello, {args.name}')
else:
    print(f'Не знаю такого языка -  {args.lang}')