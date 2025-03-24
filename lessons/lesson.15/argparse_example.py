import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help="Name of file")
parser.add_argument('--format', type=str, help="Format of output", default='txt')
parser.add_argument('--debugging', help="For debug run", action="store_true")
args = parser.parse_args()

with open(args.file, 'r') as f:
    text = f.read()

print(f'{args.file}\n{text}')

with open(f'output.{args.format}', 'w') as output:
    output.write(text)
