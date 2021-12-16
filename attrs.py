import attr
from attr import attrs

from attr import

@attrs
class Dupa:
    test: int = attr.field()


class Blada(Dupa):
    blah = attr.field()


print(attr.fields(Blada))