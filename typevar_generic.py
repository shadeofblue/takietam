from typing import TypeVar, Type


class Base:
    pass


class A(Base):

    def __init__(self, a):
        self.a = a


class B(Base):
    def __init__(self, b):
        self.b = b


class C:
    def __init__(self, c):
        self.c = c


S = TypeVar("S", bound=Base)


def instantiate(cls: Type[S], *args, **kwargs) -> S:
    return cls(*args, **kwargs)


# valid, type checkers know that a is of type A
a = instantiate(A, 1)
print(a.a)

# valid, type checkers know that b is of type B
b = instantiate(B, 2)
print(b.b)

# invalid, but type checkers still know that c is of type C
c = instantiate(C, 3)  # type: ignore
print(c.c)

