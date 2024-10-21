import enum
import json

class Status(enum.StrEnum):
    TEST = enum.auto()
    BLAH = enum.auto()

s: Status = Status.TEST
print(type(s), s, s == Status.TEST, s == "test")

print(json.dumps({"status": s}))

print(Status.TEST.value)
print(s.value == s)