import argparse


parser = argparse.ArgumentParser()
parser.add_argument("name")

parser.add_argument(
    "--lang",
    default="ru",
    choices=["ru", "en"],
    help="Язык приветствия."
)
args = parser.parse_args()

if args.lang == "ru":
    print(f'Привет, {args.name}')
elif args.lang == "en":
    print(f'Hello, {args.name}')
else:
    print('Неизвестный язык')