from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Person(_message.Message):
    __slots__ = ("id", "name", "email", "phones")
    class PhoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHONE_TYPE_UNSPECIFIED: _ClassVar[Person.PhoneType]
        PHONE_TYPE_MOBILE: _ClassVar[Person.PhoneType]
        PHONE_TYPE_HOME: _ClassVar[Person.PhoneType]
        PHONE_TYPE_WORK: _ClassVar[Person.PhoneType]
    PHONE_TYPE_UNSPECIFIED: Person.PhoneType
    PHONE_TYPE_MOBILE: Person.PhoneType
    PHONE_TYPE_HOME: Person.PhoneType
    PHONE_TYPE_WORK: Person.PhoneType
    class PhoneNumber(_message.Message):
        __slots__ = ("number", "type")
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        number: str
        type: Person.PhoneType
        def __init__(self, number: _Optional[str] = ..., type: _Optional[_Union[Person.PhoneType, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    phones: _containers.RepeatedCompositeFieldContainer[Person.PhoneNumber]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phones: _Optional[_Iterable[_Union[Person.PhoneNumber, _Mapping]]] = ...) -> None: ...

class AddressBook(_message.Message):
    __slots__ = ("people",)
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    people: _containers.RepeatedCompositeFieldContainer[Person]
    def __init__(self, people: _Optional[_Iterable[_Union[Person, _Mapping]]] = ...) -> None: ...
