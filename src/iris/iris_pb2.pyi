from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IrisPredictReply(_message.Message):
    __slots__ = ["species"]
    SPECIES_FIELD_NUMBER: _ClassVar[int]
    species: int
    def __init__(self, species: _Optional[int] = ...) -> None: ...

class IrisPredictRequest(_message.Message):
    __slots__ = ["petal_length", "petal_width", "sepal_length", "sepal_width"]
    PETAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PETAL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    SEPAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SEPAL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    petal_length: float
    petal_width: float
    sepal_length: float
    sepal_width: float
    def __init__(self, sepal_length: _Optional[float] = ..., sepal_width: _Optional[float] = ..., petal_length: _Optional[float] = ..., petal_width: _Optional[float] = ...) -> None: ...
