import argparse


parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('--lang', default='ru', help='language code')
args = parser.parse_args()
print(type(args))
print(type(args.name))

print(f'Привет, {args.name}, твой язык {args.lang}')