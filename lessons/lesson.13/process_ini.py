import configparser


def demo_configparser():
    config = configparser.ConfigParser()
    config.read("demo-config.ini")

    print("config:", config)
    print("sections:", config.sections())
    print("DEFAULT:", config["DEFAULT"])
    print("DEFAULT[environ]:", config["DEFAULT"]["environ"])
    for name, value in config["DEFAULT"].items():
        print(name, ":", value)
    print("mysql:", config["mysql"])
    for name, value in config["mysql"].items():
        print(name, ":", value)

    mysql_port = config["mysql"].get("port")
    print("mysql_port:", [mysql_port])

    postgresql_port = config["postgresql"].getint("port")
    print("postgresql_port:", [postgresql_port])

    config["mysql"]["port"] = "1122"
    config["files"]["filename"] = "spamandeggs.txt"

    with open("demo-config.ini", "w") as f:
        config.write(f)


def main():
    demo_configparser()


if __name__ == '__main__':
    main()

