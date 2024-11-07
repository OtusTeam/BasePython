import logging
from concurrent import futures
from random import randint

import grpc

from common import configure_logging
from pb import hello_pb2, hello_pb2_grpc

log = logging.getLogger(__name__)


def run() -> None:
    log.info("Start greeting")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)

        hello_request = hello_pb2.HelloRequest(name="Sam")
        hello_reply: hello_pb2.HelloReply = (
            stub.Greet(hello_request)
        )
        log.info(
            "Reply for %s: %s. Text: %r, number: %s",
            hello_request.name,
            hello_reply,
            hello_reply.hello.text,
            hello_reply.hello.number,
        )

    log.info("Finished")


def main() -> None:
    configure_logging()
    run()


if __name__ == '__main__':
    main()

