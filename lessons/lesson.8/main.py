class LowFuel(Exception):
    pass


FUEL = 10


def drive_distance(distance):
    if FUEL < 100:
        # return 0
        raise LowFuel
    return distance


def do_smth():
    drive_distance(10)


def main():
    try:
        do_smth()
    except LowFuel:
        print("Low fuel")
    else:
        print("OK")
