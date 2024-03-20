from configparser import ConfigParser
from pathlib import Path

# import os

# DB_NAME = os.environ.get('DB_NAME')
# DB_NAME = config.get("mysql", "db")

DEMO_CONFIG_FILE = "demo-config.ini"


def demo_configparser():
    config = ConfigParser()
    config.read(DEMO_CONFIG_FILE)

    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    print(dict(config["DEFAULT"]))
    print(list(config["DEFAULT"].keys()))
    print(config["DEFAULT"].get("secret_key"))

    is_debug = config.getboolean("DEFAULT", "debug")
    print("debug:", is_debug)

    for key, value in config["DEFAULT"].items():
        print(key, ":", value)

    db_conn_info = (
        config.get("mysql", "host"),
        config.getint("mysql", "port"),
    )
    print(db_conn_info)
    pg_port = config["postgresql"].getint("port")
    print(pg_port)
    pg_port += 1
    print(pg_port)

    # config.add_section("mysql")
    config["postgresql"]["port"] = str(pg_port)
    config["files"]["home"] = str(Path.home())
    config["DEFAULT"]["debug"] = str(not is_debug)

    with open(DEMO_CONFIG_FILE, "w") as f:
        config.write(f, space_around_delimiters=True)
    return config


# my_config = {
#     "DEFAULT": {
#         "debug": True,
#     },
#     "postgresql": {
#         "host": "localhost",
#         "port": 5432,
#     },
# }
# my_config["postgresql"]["port"] = 1234
# my_config["postgresql"]["db"] = "blog"


def main():
    demo_configparser()


if __name__ == "__main__":
    main()
