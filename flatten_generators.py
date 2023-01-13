from dataclasses import dataclass

@dataclass
class C:
    v: str


def process(c):
    if isinstance(c, list):
        for i in c:
            yield C(i)
    else:
        yield C(c)


def process_all(value):
    if isinstance(value[0], str):
        yield from process(value)
    else:
        for v in value:
            yield from process(v)


def load_commands(value):
    return list(process_all(value))
    # if len(value) > 0 and isinstance(value[0], str):
    #     print("str")
    #     return list(process(value))
    # else:
    #     print("list")
    #     return list(process(value))


print(load_commands(["aaaa", "bbbb", "cccc", ["eeee", "ffff"]]))

print(load_commands([["aaaa"], ["bbbb"], ["cccc"], ["eeee", "ffff"]]))

