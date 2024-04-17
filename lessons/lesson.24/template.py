import logging

from common import configure_logging

log = logging.getLogger(__name__)


def main():
    configure_logging()
    log.info("Start step ")

    log.info("End step ")



if __name__ == "__main__":
    main()
