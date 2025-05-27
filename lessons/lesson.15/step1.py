import argparse


parser = argparse.ArgumentParser()
parser.add_argument('name')
# print(parser)
args = parser.parse_args()
# print(args)

print(f'Привет, {args.name}')