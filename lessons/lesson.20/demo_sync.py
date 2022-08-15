# import logging
#
#
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
from time import sleep

from loguru import logger


def foo():
    logger.info("Start sync foo")
    sleep(1)
    logger.info("Finish sync foo")


def bar():
    logger.info("Start sync bar")
    sleep(1)
    logger.info("Finish sync bar")


def main():
    logger.info("Starting main")
    foo()
    bar()
    logger.info("Finishing main")


if __name__ == '__main__':
    main()
