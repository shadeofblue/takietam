from typing import Any, Callable, Optional, TypeVar

TReturnType = TypeVar("TReturnType")

def int_to_str(i: int) -> Optional[str]:
    if i:
        return str(i)

    return None

def str_to_int(s: str) -> Optional[int]:
    if s:
        return int(s)

    return None


def execute(c: Callable[[...], TReturnType], *args, **kwargs) -> TReturnType:
    return c(*args, **kwargs)

execute(int_to_str, 1)
execute(str_to_int, "1")


