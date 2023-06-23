# from cli import main
import os
import sys

import requests

from cli import main as cli_main


# from cli import sys


def main():
    result = requests.get('https://otus.ru')
    print(result.status_code)


# main()
cli_main()
print(sys.argv)
