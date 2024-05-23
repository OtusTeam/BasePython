from configparser import ConfigParser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FRUITS_FILE = BASE_DIR / "fruits.ini"
DEMO_CONFIG_FILE = BASE_DIR / "demo-config.ini"


def demo_fruits():
    config = ConfigParser()
    config.read(FRUITS_FILE)
    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    print(config["DEFAULT"].keys())
    print(list(config["DEFAULT"].keys()))
    print(list(config["project"].keys()))

    for section_name in config.sections():
        section = config[section_name]
        print("===", section_name)
        for key, value in section.items():
            print("+", key)
            print(value)


def demo_config():
    config = ConfigParser()
    config.read(DEMO_CONFIG_FILE)
    mysql_port = config["mysql"].getint("port")
    print(mysql_port, type(mysql_port))
    is_debug = config.getboolean("DEFAULT", "debug")
    print("is_debug", is_debug)

    mysql_port += 1
    config.set("mysql", "port", str(mysql_port))
    config["files"]["home"] = str(Path.home())

    with DEMO_CONFIG_FILE.open("w") as f:
        config.write(f)


def main():
    demo_fruits()
    demo_config()


if __name__ == "__main__":
    main()
