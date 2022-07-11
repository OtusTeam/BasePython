import configparser

DEMO_CONFIG_FILE = "demo-config.ini"


def demo_config():
    config = configparser.ConfigParser()
    config.read(DEMO_CONFIG_FILE)

    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    print(config["DEFAULT"].items())

    print("environ:", config["DEFAULT"].get("environ"))
    print("foobar:", config["DEFAULT"].get("foobar"))

    port = config["mysql"].getint("port")
    print("port:", port, type(port))

    port += 1
    print(port)

    config["mysql"]["port"] = str(port)
    config["files"]["home"] = "/home/suren"

    with open(DEMO_CONFIG_FILE, "w") as f:
        config.write(f)


def main():
    demo_config()


if __name__ == '__main__':
    main()
