from pathlib import Path

from pb import hello_pb2


HELLO_FILE = Path(__file__).parent / "hello.txt"


def write() -> None:
    # hello = hello_pb2.Hello()
    # hello.text = "Hello World!"
    hello = hello_pb2.Hello(
        text="Hello world!",
    )
    print(hello)
    print(hello.SerializeToString())
    with HELLO_FILE.open("wb") as f:
        f.write(hello.SerializeToString())


def read() -> None:
    hello = hello_pb2.Hello()
    print("hello is initialized (before):", hello.IsInitialized())
    with HELLO_FILE.open("rb") as f:
        hello.ParseFromString(f.read())
    print("hello is initialized (after):", hello.IsInitialized())
    print(hello)


def main() -> None:
    # write()
    read()


if __name__ == "__main__":
    main()

