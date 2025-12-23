from configparser import ConfigParser
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
config_path = CURRENT_DIR / "example-config.ini"


def example_read():
    config = ConfigParser()
    config.read(config_path)
    print(config.sections())
    print(config["DEFAULT"])

    print(config["DEFAULT"].keys())
    print(config["DEFAULT"].values())
    print(list(config["DEFAULT"].keys()))
    print(list(config["DEFAULT"].values()))

    print("environ:", config["DEFAULT"]["environ"])
    print([config["mysql"]["port"], config["mysql"].getint("port")])


example_read()
