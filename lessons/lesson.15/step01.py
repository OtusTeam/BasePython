import argparse


parser = argparse.ArgumentParser()
parser.add_argument('name') # python script.py Боб
args = parser.parse_args()

print(f'Привет {args.name}')

