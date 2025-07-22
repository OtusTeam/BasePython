import argparse


parser = argparse.ArgumentParser()
parser.add_argument('name', help="Имя пользователя") # python script.py Боб
parser.add_argument('--lang', default='ru', help='Язык программы') # python script.py Боб
args = parser.parse_args()

if args.lang == "ru":
    print(f'Привет, {args.name} - язык {args.lang}')
elif args.lang == "en":
    print(f'Hello, {args.name} - язык {args.lang}')
else:
    print(f'Не известный язык {args.lang}')


