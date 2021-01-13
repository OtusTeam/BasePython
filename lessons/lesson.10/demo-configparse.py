import configparser


def demo_configparser():
    config = configparser.ConfigParser()
    config.read("demo-config.ini")
    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    for item in config["DEFAULT"].items():
        print(item)

    print("pg secret key", config["postgresql"]["secret_key"])
    # for item in config["postgresql"].items():
    #     print(item)

    print("mysql")
    print("port:", [config["mysql"].get("port", "1234")])
    print("pg port:", [config["postgresql"].getint("port", 1589)])

    config["mysql"]["port"] = "5667"

    with open("demo-config.ini", "w") as f:
        config.write(f)


if __name__ == '__main__':
    demo_configparser()
