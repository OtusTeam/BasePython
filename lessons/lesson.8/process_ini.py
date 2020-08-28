import configparser


def demo_configparser():
    config = configparser.ConfigParser()
    config.read("demo-config.ini")
    print(config)
    print(config.sections())

    print(list(config))
    psql = config["postgresql"]
    print("PSQL:", psql)
    for key in psql:
        print(key, psql[key])

    psql_host = psql["host"]
    print(psql_host)
    psql_user = config["postgresql"]["user"]
    print(psql_user)

    psql_port = psql.get("port", 5432)
    print(psql_port)

    config["postgresql"]["port"] = str(psql_port)

    with open("demo-config.ini", "w") as f:
        config.write(f)


if __name__ == '__main__':
    demo_configparser()
