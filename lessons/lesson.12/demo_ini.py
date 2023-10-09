import configparser
from pathlib import Path

DEMO_CONFIG = "demo-config.ini"


def demo_configparser():
    config = configparser.ConfigParser()
    config.read(DEMO_CONFIG)
    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    print("environ:", config["DEFAULT"]["environ"])

    for key, value in config["DEFAULT"].items():
        print(key, value)

    mysql_port = config["mysql"].getint("port")
    print(mysql_port)
    # print([mysql_port])
    mysql_port += 1

    config["mysql"]["port"] = str(mysql_port)

    config["files"]["home"] = str(Path.home())

    with open(DEMO_CONFIG, "w") as file:
        config.write(file, space_around_delimiters=True)


if __name__ == "__main__":
    demo_configparser()
