from typing import TypedDict, NotRequired

class Foo(TypedDict):
    bar: int
    baz: NotRequired[str]

def my_method(foo: Foo):
    ...

# Usage
my_method(foo={
    "bar": "test"
})

