import logging
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
)
log = logging.getLogger(__name__)


def get_users():
    log.info("get users")
    sleep(1)
    log.info("fetched users")


def get_weather():
    log.info("get weather")
    sleep(1)
    log.info("fetched weather")


def main():
    log.info("Start")
    get_users()
    get_weather()
    log.info("Done")


if __name__ == "__main__":
    main()
