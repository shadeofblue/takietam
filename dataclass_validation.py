from dataclasses import dataclass

@dataclass
class Test:
    foo: int

# doesn't cause an error :(
print(Test("aaa"))