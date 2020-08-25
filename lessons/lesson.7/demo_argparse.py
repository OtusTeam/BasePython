import os
import argparse
import sys

print(sys.argv)


def demo_base_parse():
    parser = argparse.ArgumentParser(
        prog="My argparse demo",
        description="Show argparse",
    )

    parser.add_argument(
        "path",
        metavar="path",
        type=str,
        help="the path to be listed"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="verbose show more info"
    )

    args = parser.parse_args()

    print(args)

    if args.verbose:
        print("Gonna list this dir", args.path)

    if not os.path.isdir(args.path):
        if args.verbose:
            print("No such directory")
        sys.exit(1)

    print(os.listdir(args.path))


parser = argparse.ArgumentParser(
    prog="Demo actions",
    description="Demo all available parser actions",
    epilog="Happy learning!",
)
parser.version = "0.1.0"
parser.add_argument(
    "-V",
    # "--version",
    action="version",
)
parser.add_argument(
    "--no-run",
    action="store_true",
)

parser.add_argument(
    "-qwerty",
    action="store_false",
)

parser.add_argument(
    "-n",
    "--name",
    action="store",
)

parser.add_argument(
    "-k",
    action="store_const",
    const=42,
)

parser.add_argument(
    "-a",
    "--append-val",
    action="append",
    help="append values",
)

parser.add_argument(
    "-ac",
    action="append_const",
    const="spam and eggs",
)

parser.add_argument(
    "-i",
    "--info",
    action="help",
    help="Alternative help call",
)

parser.add_argument(
    "-c",
    action="count",
)

args = parser.parse_args()
print(args)

if args.no_run:
    print("no run selected! leaving")
    sys.exit()


print("others..")
