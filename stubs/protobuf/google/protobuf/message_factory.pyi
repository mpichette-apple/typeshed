from collections.abc import Iterable
from typing import Any

from google.protobuf.descriptor import Descriptor
from google.protobuf.descriptor_pb2 import FileDescriptorProto
from google.protobuf.descriptor_pool import DescriptorPool
from google.protobuf.message import Message

class MessageFactory:
    pool: Any
    def __init__(self, pool: DescriptorPool | None = ...) -> None: ...
    def GetPrototype(self, descriptor: Descriptor) -> type[Message]: ...
    def GetMessages(self, files: Iterable[str]) -> dict[str, type[Message]]: ...

def GetMessageClass(descriptor: Descriptor) -> type[Message]: ...

def GetMessageClassesForFiles(files: Iterable[str], pool: DescriptorPool) -> dict[str, type[Message]]: ...

def GetMessages(file_protos: Iterable[FileDescriptorProto], pool: DescriptorPool | None = ...) -> dict[str, type[Message]]: ...
