from dataclasses import dataclass

foo = "test"
bar = b"blah\nblahblah"

@dataclass
class Dupa:
    test: str

dupa = Dupa(test="sfsafas")

print(f"{foo=}, {bar=}, {dupa=}, {dupa.test=}")
