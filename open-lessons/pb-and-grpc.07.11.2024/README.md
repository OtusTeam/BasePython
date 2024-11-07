# Знакомство с Protobuf и gRPC. Работа с gRPC на Python


## Ссылки
- https://grpc.github.io/grpc/core/md_doc_g_stands_for.html
- https://grpc.io/docs/languages/python/quickstart/
- https://github.com/protocolbuffers/protobuf/releases/tag/v26.0
- https://protobuf.dev/getting-started/pythontutorial/
- https://github.com/grpc/grpc/tree/master/examples/python

## Шаги

- настроили Poetry
- установили Python пакет `protobuf`
- поставили protobuf на macOS командой
    ```shell
    brew install protobuf
    ```
- компилируем протокол на Python
    ```shell
    protoc --proto_path=protos --python_out=./pb protos/hello.proto
    ```
- компилируем протокол в Python плюс аннотации типов
    ```shell
    protoc --proto_path=protos --python_out=./pb --pyi_out=./pb protos/hello.proto
    ```
- установили Python пакет `grpcio`
- установили Python пакет `grpcio-tools`
- описали сервис `Greeter`
- компилируем командой
    ```shell
    python -m grpc_tools.protoc --proto_path=protos --python_out=./pb --pyi_out=./pb --grpc_python_out=./pb protos/hello.proto
    ```
- правим импорт
- реализуем сервисер
- запускаем сервер
- вызываем клиент


Example stream:
```python
# client
def request_iter():
    for idx in range(5):
        yield service_pb2.HelloRequest(name=f"Stream #{idx}")


stub.GreetStream(request_iter())

# server
for r in request_iter:
    print(f"Stream request {r}")
    yield service_pb2.HelloReply(message=f"Hello, {r.name}!")
```
