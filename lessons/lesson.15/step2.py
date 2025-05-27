import argparse


parser = argparse.ArgumentParser()
parser.add_argument("name", help='Имя пользователя')
parser.add_argument("age", help='Имя пользователя')
parser.add_argument("--lang", default="ru", choices=["ru", "en", "cn"],  help='Язык пользователя')
args = parser.parse_args()
print(args)

args_dict = vars(args)
print(type(args_dict))
print(args_dict)

if args.lang == "ru":
    print(f'Привет, {args.name} {args.age}')
elif args.lang == "en":
    print(f'Hello, {args.name} {args.age}')
else:
    print(f'Неизвестный язык, {args.name} {args.age}')
