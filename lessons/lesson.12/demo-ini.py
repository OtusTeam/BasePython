import configparser

DEMO_CONFIG_FILE = "demo-config.ini"


def demo_config():
    config = configparser.ConfigParser()
    config.read(DEMO_CONFIG_FILE)
    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    print(config["DEFAULT"]["secret_key"])

    print("default params:")
    for key, value in config["DEFAULT"].items():
        print(key, value)

    mysql_port = config["mysql"].getint("port")
    print(mysql_port, type(mysql_port))
    mysql_port += 1
    print(mysql_port)
    config["mysql"]["port"] = str(mysql_port)

    config["files"]["home"] = "/home/Suren"

    with open(DEMO_CONFIG_FILE, "w") as f:
        config.write(f, space_around_delimiters=True)


if __name__ == "__main__":
    demo_config()

