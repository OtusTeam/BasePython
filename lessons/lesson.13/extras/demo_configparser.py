import configparser
from pathlib import Path

BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / "demo-config.ini"


def demo_configparser():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    for section_name, section in config.items():
        print(section_name)
        print(section)
        print(dict(section))
        # for name, value in section.items():
        #     print(name, ":", value)

    print()
    print(config["DEFAULT"])

    # mysql_port = config["mysql"]["port"]
    mysql_port = config["mysql"].getint("port")
    # print(mysql_port, repr(mysql_port))
    mysql_port += 1
    config["mysql"]["port"] = str(mysql_port)

    config["files"]["home"] = str(Path.home())

    # print(config)
    with open(CONFIG_FILE, "w") as file:
        config.write(file, space_around_delimiters=True)


if __name__ == "__main__":
    demo_configparser()
