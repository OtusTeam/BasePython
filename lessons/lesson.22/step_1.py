import logging
from time import sleep

logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


def get_users():
    log.info("Starting fetching users")
    sleep(1)
    log.info("Finished fetching users")


def get_products():
    log.info("Starting fetching products")
    sleep(1)
    log.info("Finished fetching products")


def main():
    log.info("Start")
    get_users()
    get_products()
    log.info("Finish")


if __name__ == "__main__":
    main()
