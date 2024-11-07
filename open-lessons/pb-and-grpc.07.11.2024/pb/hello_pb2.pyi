from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Hello(_message.Message):
    __slots__ = ("text", "number")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    text: str
    number: int
    def __init__(self, text: _Optional[str] = ..., number: _Optional[int] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ("hello",)
    HELLO_FIELD_NUMBER: _ClassVar[int]
    hello: Hello
    def __init__(self, hello: _Optional[_Union[Hello, _Mapping]] = ...) -> None: ...
