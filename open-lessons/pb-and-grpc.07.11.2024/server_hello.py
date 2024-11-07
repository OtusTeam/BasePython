import logging
from concurrent import futures
from random import randint

import grpc

from common import configure_logging
from pb import hello_pb2, hello_pb2_grpc

log = logging.getLogger(__name__)


class GreeterServicer(hello_pb2_grpc.GreeterServicer):

    def Greet(
        self,
        request: hello_pb2.HelloRequest,
        context: grpc.ServicerContext,
    ) -> hello_pb2.HelloReply:
        log.info(
            "Received hello request for name %r",
            request.name,
        )
        hello = hello_pb2.Hello(
            text=f"Hello, {request.name}!",
            number=randint(1, 100),
        )
        reply = hello_pb2.HelloReply(hello=hello)
        log.info("Respond with %r", reply)
        return reply


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(
        GreeterServicer(),
        server,
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    log.warning("Listening on port 50051")
    server.wait_for_termination()


def main() -> None:
    configure_logging()
    try:
        serve()
    except KeyboardInterrupt:
        log.warning('Received keyboard interrupt.')


if __name__ == '__main__':
    main()

