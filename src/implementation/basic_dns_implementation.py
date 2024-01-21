from dataclasses import dataclass
import dataclasses
import struct


# Dataclass will hold only the data
@dataclass
class DNSHeader:
    """
    Request header will look like this
    """
    id: int
    flags: int
    num_questions: int = 0
    num_answers: int = 0
    num_authorities: int = 0
    num_additionals: int = 0


@dataclass
class DNSQuestion:
    """
    name: Name of the domain
    type_: A -> Ipv4 "A"ddress
    class_: IN -> Internet

    """
    name: bytes
    type_: int
    class_: int


def header_to_bytes(header):
    fields = dataclasses.astuple(header)
    return struct.pack("!HHHHHH", *fields)


def question_to_bytes(question):
    return question.name + struct.pack("!HH", question.type_, question.class_)
