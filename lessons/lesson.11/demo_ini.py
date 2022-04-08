import configparser


DEMO_CONFIG_INI_FILE = "demo-config.ini"


def demo_configparser():
    config = configparser.ConfigParser()
    config.read(DEMO_CONFIG_INI_FILE)

    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    print(list(config["DEFAULT"].items()))
    # print(config["DEFAULT"]["environ"])
    print(config["DEFAULT"].get("environ"))

    # port = config["mysql"]["port"]
    # config["qwerty"]
    port = config["mysql"].getint("port")
    print(port)
    port += 1
    print(port)

    config["mysql"]["port"] = str(port)
    config["files"]["filename"] = "foobar.txt"

    with open(DEMO_CONFIG_INI_FILE, "w") as f:
        config.write(f)
        # f.write("text")


def main():
    demo_configparser()


if __name__ == '__main__':
    main()
