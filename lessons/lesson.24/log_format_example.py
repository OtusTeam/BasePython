import logging
import time

from common import configure_logging

log = logging.getLogger(__name__)


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        time.sleep(1)
        return f"User(user_id={self.user_id!r})"


def main():
    configure_logging(level=logging.INFO)
    log.warning("Start")
    user_john = User("john")
    user_sam = User("sam")
    # log.info("Created user %s", user_john)
    # log.info(f"Created user {user_john}")
    for user in (user_john, user_sam):
        log.info("Created user id = %r", user.user_id)
        # log.info(f"Created user id = {user.user_id!r}")

    log.warning("End")


if __name__ == '__main__':
    main()
