import configparser

DEMO_CONFIG_FILE = "demo-config.ini"


def demo_config():
    config = configparser.ConfigParser()
    config.read(DEMO_CONFIG_FILE)
    print(config)
    print(config["DEFAULT"])
    print(config["DEFAULT"].items())
    print(dict(config["DEFAULT"].items()))
    print(config["DEFAULT"].keys())
    print(list(config["DEFAULT"].keys()))
    print(config["DEFAULT"]["secret_key"])
    print(config["DEFAULT"].get("hello"))
    print(config["DEFAULT"].get("hello", "default"))
    print(config["DEFAULT"].get("environ"))

    port = config["mysql"].getint("port")
    # port = config["mysql"].get("port")
    print(port, type(port))

    port += 1
    print(port)
    config["mysql"]["port"] = str(port)
    config["files"]["home"] = "/home/suren"

    with open(DEMO_CONFIG_FILE, "w") as f:
        config.write(f)


if __name__ == "__main__":
    demo_config()
