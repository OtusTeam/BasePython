import configparser


def demo_configparser():
    config = configparser.ConfigParser()
    config.read("demo-config.ini")
    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    # print(type(config["DEFAULT"]))
    # print(type(config["DEFAULT"]).__mro__)
    for item in config["DEFAULT"].items():
        print(item)

    print("PG sk:", config["postgresql"]["secret_key"])
    mysql_port = config["mysql"].get("port", "5678")
    print("mysql port:", [mysql_port])
    pg_port = config["postgresql"].getint("port", 5432)
    print("pg port:", [pg_port])
    config["mysql"]["port"] = "7654"

    with open("demo-config.ini", "w") as f:
        config.write(f)


if __name__ == '__main__':
    demo_configparser()
